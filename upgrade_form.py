import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the mailto block with Fetch API logic
old_logic = '''      // Construct mailto link
      const emailRecipient = 'aayushtyagi728@gmail.com';
      const mailtoSubject = encodeURIComponent([Portfolio Inquiry] Message from );
      
      let emailBody = Hello Aayush,\\n\\n + 
                        You have received a new inquiry from your portfolio website.\\n\\n +
                        Name: \\n +
                        Email: \\n;
                        
      if (phoneNumber) {
        emailBody += Phone: \\n;
      }
      
      emailBody += \\nMessage:\\n\\n\\n +
                   Best regards,\\n +
                   ${fullName};
                         
      const mailtoBody = encodeURIComponent(emailBody);
      
      // Open mail client
      window.location.href = mailto:aayushtyagi728@gmail.com?subject=&body=;'''

# We need to escape backticks properly in python
new_logic = '''      // Send email silently via FormSubmit API
      const btn = contactForm.querySelector('button[type="submit"]');
      const originalText = btn.innerHTML;
      btn.innerHTML = '<span>Sending...</span>';
      
      fetch('https://formsubmit.co/ajax/aayushtyagi728@gmail.com', {
          method: 'POST',
          headers: { 
              'Content-Type': 'application/json',
              'Accept': 'application/json'
          },
          body: JSON.stringify({
              name: fullName,
              email: emailAddress,
              phone: phoneNumber || 'Not provided',
              message: message,
              _subject: New Portfolio Message from 
          })
      })
      .then(response => response.json())
      .then(data => {
          btn.innerHTML = '<span>Sent Successfully! ?</span>';
          btn.style.borderColor = 'var(--accent-gold-light)';
          btn.style.color = 'var(--accent-gold-light)';
          contactForm.reset();
          setTimeout(() => {
              btn.innerHTML = originalText;
              btn.style.borderColor = '';
              btn.style.color = '';
          }, 4000);
      })
      .catch(error => {
          alert('Oops! There was a problem submitting your form. Please try again.');
          btn.innerHTML = originalText;
      });'''

js = js.replace(old_logic, new_logic)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Form upgraded")
