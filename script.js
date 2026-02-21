// Simple client-side form handler
const form = document.getElementById('contact-form');
const formMessage = document.getElementById('form-message');

form.addEventListener('submit', function(e) {
  e.preventDefault();
  formMessage.textContent = 'Thank you for reaching out! I will get back to you soon.';
  form.reset();
});
