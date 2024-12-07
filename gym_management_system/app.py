from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__,template_folder='template')

# Configure Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # For Gmail, you can also use other SMTP services
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sjagadeeshw@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'ufjuejldnuudunqm'  # Your email password (use an app-specific password if using Gmail)

# Initialize Flask-Mail
mail = Mail(app)

# Route to display the contact form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create the email content
        msg = Message(
            'New Contact Form Submission', 
            sender=email,  # Sender's email
            recipients=['sjagadeeshw@gmail.com']  # Admin email where the message will be sent
        )
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Send the email
        try:
            mail.send(msg)
            return redirect(url_for('thank_you'))  # Redirect to a thank-you page
        except Exception as e:
            return f"Error: {str(e)}"

# Thank you page after successful submission
@app.route('/thank-you')
def thank_you():
    return "Thank you for contacting us! We will get back to you shortly."

if __name__ == '__main__':
    app.run(debug=True)
