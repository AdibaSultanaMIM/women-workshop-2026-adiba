
// Registration Form Handler for WE-ICT 2026
// API Configuration - Update this URL after deploying backend to PythonAnywhere
const API_URL = 'https://sultana2016.pythonanywhere.com';

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registrationForm');
    const submitBtn = document.getElementById('submitRegBtn');
    const successMsg = document.getElementById('regSuccessMsg');
    const errorMsg = document.getElementById('regErrorMsg');

    if (!form) {
        console.error('Registration form not found');
        return;
    }

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Hide previous messages
        successMsg.style.display = 'none';
        errorMsg.style.display = 'none';
        
        // Disable button and show loading
        submitBtn.disabled = true;
        submitBtn.querySelector('.btn-text').style.display = 'none';
        submitBtn.querySelector('.btn-loader').style.display = 'inline';
        
        // Collect form data
        const formData = {
            full_name: document.getElementById('reg_full_name').value.trim(),
            email: document.getElementById('reg_email').value.trim().toLowerCase(),
            phone: document.getElementById('reg_phone').value.trim(),
            institution: document.getElementById('reg_institution').value.trim(),
            topic: document.getElementById('reg_topic').value
        };
        
        // Basic client-side validation
        if (!validateEmail(formData.email)) {
            showError('Please enter a valid email address');
            resetButton();
            return;
        }
        
        if (!validatePhone(formData.phone)) {
            showError('Please enter a valid 11-digit phone number');
            resetButton();
            return;
        }
        
        try {
            const response = await fetch(`${API_BASE_URL}/register`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            
            if (response.ok) {
                showSuccess(data.message || 'Registration successful! Check your email for confirmation.');
                form.reset();
                
                // Scroll to success message
                setTimeout(() => {
                    successMsg.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }, 100);
            } else {
                throw new Error(data.error || 'Registration failed');
            }
        } catch (error) {
            console.error('Registration error:', error);
            showError(error.message || 'Unable to connect to server. Please try again later.');
        } finally {
            resetButton();
        }
    });
    
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    function validatePhone(phone) {
        return /^[0-9]{11}$/.test(phone);
    }
    
    function showSuccess(message) {
        document.getElementById('successText').textContent = message;
        successMsg.style.display = 'flex';
    }
    
    function showError(message) {
        document.getElementById('errorText').textContent = message;
        errorMsg.style.display = 'flex';
    }
    
    function resetButton() {
        submitBtn.disabled = false;
        submitBtn.querySelector('.btn-text').style.display = 'inline';
        submitBtn.querySelector('.btn-loader').style.display = 'none';
    }
});
