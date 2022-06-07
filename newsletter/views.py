from django.core.mail import send_mass_mail
from newsletter.models import Subscriber


def send_newsletter(request):
    if request.method == 'POST':
        emails_subscribers = Subscriber.objects.values_list('user__email')
        emails_subscribers_list = [x for x in emails_subscribers.iterator()]
        send_mass_mail(
            request.POST['subject'],
            request.POST['message'],
            'no-reply@ecommerce.com',
            emails_subscribers_list,
        )
