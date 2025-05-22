 // static/js/material.js
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const menuButton = document.querySelector('.md-menu-button');
    const drawer = document.querySelector('.md-drawer');
    const closeDrawer = document.querySelector('.md-drawer-header .material-icons');
    
    if (menuButton && drawer && closeDrawer) {
        menuButton.addEventListener('click', function() {
            drawer.classList.add('open');
        });
        
        closeDrawer.addEventListener('click', function() {
            drawer.classList.remove('open');
        });
    }
    
    // Close messages
    const messageCloseButtons = document.querySelectorAll('.md-message-close');
    
    messageCloseButtons.forEach(button => {
        button.addEventListener('click', function() {
            const message = this.parentElement;
            message.style.opacity = '0';
            setTimeout(() => {
                message.style.display = 'none';
            }, 300);
        });
    });
    
    // Mobile chat sidebar toggle
    const chatToggleButton = document.createElement('button');
    chatToggleButton.className = 'md-button md-button-icon md-chat-toggle';
    chatToggleButton.innerHTML = '<span class="material-icons">people</span>';
    chatToggleButton.setAttribute('aria-label', 'Toggle Contacts');
    
    const chatArea = document.querySelector('.md-chat-area');
    const chatSidebar = document.querySelector('.md-chat-sidebar');
    
    if (chatArea && chatSidebar && window.innerWidth <= 768) {
        chatArea.appendChild(chatToggleButton);
        
        chatToggleButton.addEventListener('click', function() {
            chatSidebar.classList.toggle('active');
        });
    }
    
    // Form input animation
    const formInputs = document.querySelectorAll('.md-form-input');
    
    formInputs.forEach(input => {
        if (input.value) {
            input.classList.add('has-value');
        }
        
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
            if (this.value) {
                this.classList.add('has-value');
            } else {
                this.classList.remove('has-value');
            }
        });
    });
});
