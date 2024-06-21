from django.shortcuts import render
from backend.models import Tileproducts,Projects
from django.core.mail import send_mail

from django.core import mail
connection = mail.get_connection()  # Use default email connection




# Create your views here.
from backend.forms import FeedbackForm
def homePage(request):
    

    # Creating a dictionary to pass as an argument
    query_results=Tileproducts.objects.all()
    query_results2=Projects.objects.all()
    contextcontent = { 'query_results' : query_results, 'query2':query_results2 }
    return render(request,template_name="homePage.html",context=contextcontent)


def aboutPage(request):
    return render(request,template_name="aboutPage.html")


def contactPage(request):
    form = FeedbackForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            feedback = form.cleaned_data
            user_name=feedback['contact_name']
            user_email=feedback['contact_email']
            subject=f"{user_name} has shared a feeback!"
            content=feedback['content']

      
            send_mail(
            subject,
            content,
            user_email,
            ["revadibrunda@gmail.com","pratikram.design@gmail.com"],
            fail_silently=False,
            connection=connection
        )
            form.clean()
            
            

    context = {'form': form}
    return render(request,template_name="contactPage.html",context=context)
