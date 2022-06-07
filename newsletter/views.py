from django.http import HttpResponse
from django.core.mail import send_mass_mail
from newsletter.models import Subscriber


def send_newsletter(request):
    if request.user.is_staff is False:
        return HttpResponse('You do not have permission to perform this action')
    if request.method == 'POST':
        emails_subscribers = Subscriber.objects.values_list('user__email')
        emails_subscribers_list = [x.email for x in emails_subscribers.iterator()]
        send_mass_mail(
            request.POST['subject'],
            request.POST['message'],
            'no-reply@ecommerce.com',
            emails_subscribers_list,
        )
        return HttpResponse('Mail sent to subscribers')
