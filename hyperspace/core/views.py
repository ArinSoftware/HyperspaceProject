from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from services.models import Service
from blog.models import Blog

def index(request):
    # Define your static content
    static_content = """
    <div class="inner">
        <h1>Hyperspace</h1>
        <p>Just another fine responsive site template designed by <a href="http://html5up.net">HTML5 UP</a><br />
        and released for free under the <a href="http://html5up.net/license">Creative Commons</a>.</p>
        <ul class="actions">
            <li><a href="#one" class="button scrolly">Learn more</a></li>
        </ul>
    </div>
    """

    featured_services = Service.objects.filter(is_featured=True)
    latest_posts = Blog.objects.all()[:3]
    context = {'static_content': static_content, 'featured_services': featured_services, 'latest_posts': latest_posts}

    return render(request, 'core/index.html', context)

def contact(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Compose the message
        subject = f"New contact form submission from {name}"
        message_body = f"Message from {name} ({email}):\n\n{message}"
        recipient_list = [settings.EMAIL_HOST_USER]  # Your email

        # Send email to admin
        try:
            send_mail(subject, message_body, email, recipient_list)
        except Exception as err:
            messages.error(request, "Something happened, please try again later")
        else:
            messages.success(request, "We have received your email successfully!")
        
    return HttpResponseRedirect(reverse('index') + '#three')
