from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_view, name='chat_view'),
    path('chat/<int:user_id>/', views.chat_view, name='chat_with_user'),
    path('send/<int:user_id>/', views.send_message, name='send_message'),
    path('add-contact/', views.add_contact, name='add_contact'),
    path('accept-invite/<int:invite_id>/', views.accept_invite, name='accept_invite'),
    path('decline-invite/<int:invite_id>/', views.decline_invite, name='decline_invite'),
    path('get-messages/<int:user_id>/', views.get_messages, name='get_messages'),
]
