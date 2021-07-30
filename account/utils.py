from django.core.mail import send_mail


def send_welcome_email(email):
    url = 'http://localhost:8000/'
    message = f'<h1>Thanks for registration on site PyShop12!</h1> \n {url}'
    send_mail('PyShop12 Welcome!',
              message,
              'eelonmusk@gmail.com',
              [email,],
              fail_silently=False
              )
