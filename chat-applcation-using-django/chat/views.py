# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .models import Profile, Contact, Message, ChatInvite
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core import serializers

def home_view(request):
    if request.user.is_authenticated:
        return redirect('chat:chat_view')
    return render(request, 'home.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('chat:chat_view')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                Profile.objects.get_or_create(user=user)
                login(request, user)
                messages.success(request, "Registration successful!")
                return redirect('chat:chat_view')
            except IntegrityError:
                messages.error(request, "A profile for this user already exists.")
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('chat:chat_view')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # Ensure a profile exists for the user
                Profile.objects.get_or_create(user=user)
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('chat:chat_view')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')

@login_required
def chat_view(request, user_id=None):
    contacts = Contact.objects.filter(user=request.user).select_related('contact')
    
    # Get all users that have exchanged messages with the current user
    message_partners = User.objects.filter(
        Q(sent_messages__receiver=request.user) | 
        Q(received_messages__sender=request.user)
    ).distinct().exclude(id=request.user.id)
    
    # Combine contacts and message partners
    chat_users = set([contact.contact for contact in contacts])
    chat_users.update(message_partners)
    
    active_chat = None
    messages_list = []
    
    if user_id:
        chat_partner = get_object_or_404(User, id=user_id)
        active_chat = chat_partner
        
        # Get messages between the current user and the selected user
        messages_list = Message.objects.filter(
            (Q(sender=request.user) & Q(receiver=chat_partner)) |
            (Q(sender=chat_partner) & Q(receiver=request.user))
        ).order_by('timestamp')
        
        # Mark messages as read
        unread_messages = messages_list.filter(is_read=False, receiver=request.user)
        unread_messages.update(is_read=True)
    
    # Get pending invites for the logged-in user
    pending_invites = ChatInvite.objects.filter(to_user=request.user, accepted=False, declined=False)
    
    context = {
        'contacts': chat_users,
        'active_chat': active_chat,
        'messages': messages_list,
        'pending_invites': pending_invites,
    }
    
    return render(request, 'chat/chat.html', context)

@login_required
def send_message(request, user_id):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        content = request.POST.get('content')
        receiver = get_object_or_404(User, id=user_id)
        
        if content:
            message = Message.objects.create(
                sender=request.user,
                receiver=receiver,
                content=content
            )
            
            return JsonResponse({
                'status': 'success',
                'message': {
                    'id': message.id,
                    'content': message.content,
                    'timestamp': message.timestamp.strftime('%H:%M'),
                    'is_sender': True
                }
            })
    
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def add_contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            contact_user = User.objects.get(username=username)
            if contact_user != request.user:
                # Create a chat invite instead of direct contact
                invite, created = ChatInvite.objects.get_or_create(from_user=request.user, to_user=contact_user)
                if created:
                    messages.success(request, f"Invite sent to {username}!")
                else:
                    messages.info(request, f"You have already sent an invite to {username}.")
            else:
                messages.error(request, "You cannot add yourself as a contact.")
        except User.DoesNotExist:
            messages.error(request, f"User {username} does not exist.")
    return redirect('chat:chat_view')

@login_required
def accept_invite(request, invite_id):
    invite = get_object_or_404(ChatInvite, id=invite_id, to_user=request.user)
    if request.method == 'POST':
        invite.accepted = True
        invite.save()
        # Create contact both ways
        Contact.objects.get_or_create(user=request.user, contact=invite.from_user)
        Contact.objects.get_or_create(user=invite.from_user, contact=request.user)
        messages.success(request, f"You are now contacts with {invite.from_user.username}!")
    return redirect('chat:chat_view')

@login_required
def decline_invite(request, invite_id):
    invite = get_object_or_404(ChatInvite, id=invite_id, to_user=request.user)
    if request.method == 'POST':
        invite.declined = True
        invite.save()
        messages.info(request, f"You declined the invite from {invite.from_user.username}.")
    return redirect('chat:chat_view')

@login_required
def get_messages(request, user_id):
    chat_partner = get_object_or_404(User, id=user_id)
    messages_list = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=chat_partner)) |
        (Q(sender=chat_partner) & Q(receiver=request.user))
    ).order_by('timestamp')
    messages_data = [
        {
            'id': msg.id,
            'sender': msg.sender.username,
            'receiver': msg.receiver.username,
            'content': msg.content,
            'timestamp': msg.timestamp.strftime('%H:%M'),
            'is_sender': msg.sender == request.user
        }
        for msg in messages_list
    ]
    return JsonResponse({'messages': messages_data})
