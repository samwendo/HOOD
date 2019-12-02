from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name, receiver):
    #Creating message subject and sender
    subject = 'HOOD Account creation successful'
    sender = 'wendosam21@gmail.com'

    #passing in the context variables
    text_context = render_to_string('email/welcomeemail.txt', {"name":name})
    html_content = render_to_string('email/welcomeemail.html',{"name":name})

    msg = EmailMultiAlternatives(subject, text_context, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
