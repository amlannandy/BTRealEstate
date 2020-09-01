from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made a enquiry')
                return redirect('/listings/' + listing_id)

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )
        contact.save()
        send_mail(
            subject='Property listing enquiry - ' + listing,
            message=name + ' has made an inquiry for listing - ' + listing,
            from_email='complexityteambbsr@gmail.com',
            recipient_list=[realtor_email, 'amlannandy5@gmail.com'],
            fail_silently=False
        )
        messages.success(request, 'Inquiry saved')
        return redirect('/listings/' + listing_id)
