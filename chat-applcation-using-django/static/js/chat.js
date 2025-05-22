document.addEventListener('DOMContentLoaded', function() {
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const messagesContainer = document.getElementById('messages-container');
    
    if (messageForm && messageInput && messagesContainer) {
        // Auto-scroll to bottom of messages
        function scrollToBottom() {
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
        
        scrollToBottom();
        
        // Handle message submission
        messageForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const userId = this.getAttribute('data-user-id');
            const content = messageInput.value.trim();
            
            if (!content || !userId) return;
            
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            
            // Create a FormData object
            const formData = new FormData();
            formData.append('content', content);
            
            // Send message via fetch API
            fetch(`/chat/send/${userId}/`, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                },
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.status === 'success') {
                    // Create and append new message element
                    const messageCard = document.createElement('div');
                    messageCard.className = 'md-message-card md-message-sent';
                    
                    const messageContent = document.createElement('div');
                    messageContent.className = 'md-message-content';
                    messageContent.textContent = data.message.content;
                    
                    const messageTime = document.createElement('div');
                    messageTime.className = 'md-message-time';
                    messageTime.textContent = data.message.timestamp;
                    
                    messageCard.appendChild(messageContent);
                    messageCard.appendChild(messageTime);
                    messagesContainer.appendChild(messageCard);
                    
                    // Clear input field
                    messageInput.value = '';
                    
                    // Scroll to bottom
                    scrollToBottom();
                }
            })
            .catch(error => {
                console.error('Error sending message:', error);
                // Display error notification
                const errorNotification = document.createElement('div');
                errorNotification.className = 'md-message md-message-error';
                errorNotification.textContent = 'Failed to send message. Please try again.';
                document.querySelector('.md-messages').appendChild(errorNotification);
                
                // Remove notification after 3 seconds
                setTimeout(() => {
                    errorNotification.remove();
                }, 2000);
            });
        });
        
        // Poll for new messages every 3 seconds (would be better with WebSockets)
        function pollMessages() {
            const userId = messageForm.getAttribute('data-user-id');
            if (!userId) return;
            
            const lastMessageId = document.querySelector('.md-message-card:last-child')?.dataset.messageId || 0;
            
            fetch(`/chat/messages/${userId}/?last_id=${lastMessageId}`, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.messages && data.messages.length > 0) {
                    data.messages.forEach(message => {
                        const messageCard = document.createElement('div');
                        messageCard.className = `md-message-card ${message.is_sender ? 'md-message-sent' : 'md-message-received'}`;
                        messageCard.dataset.messageId = message.id;
                        
                        const messageContent = document.createElement('div');
                        messageContent.className = 'md-message-content';
                        messageContent.textContent = message.content;
                        
                        const messageTime = document.createElement('div');
                        messageTime.className = 'md-message-time';
                        messageTime.textContent = message.timestamp;
                        
                        messageCard.appendChild(messageContent);
                        messageCard.appendChild(messageTime);
                        messagesContainer.appendChild(messageCard);
                    });
                    
                    scrollToBottom();
                }
            })
            .catch(error => {
                console.error('Error polling messages:', error);
            });
        }
        
        // Start polling
        setInterval(pollMessages, 2000);
    }
    
    // Mobile chat sidebar toggle
    const chatToggleButton = document.querySelector('.md-chat-toggle');
    const chatSidebar = document.querySelector('.md-chat-sidebar');
    
    if (chatToggleButton && chatSidebar) {
        chatToggleButton.addEventListener('click', function() {
            chatSidebar.classList.toggle('active');
        });
    }
});
