from django.shortcuts import render
from django.shortcuts import redirect, render
from backend.forms import ContactForm
from .models import Tileproducts,Projects
from django.views.generic import ListView,DetailView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# for tile products
class HomeView(ListView):
    model=Tileproducts
    template_name="products.html"
    context_object_name='tileproducts'


class DetailViews(DetailView):
    model=Tileproducts
    template_name="product_detail.html"
    context_object_name='item'

# for tile projects

class HomeViewProject(ListView):
    model=Projects
    template_name="projects.html"
    context_object_name='projects'



class JsonableResponseMixin:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.accepts("text/html"):
            return response
        else:
            return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        if form.is_valid():
            print("FORM is valid")
            feedback = form.cleaned_data
            user_name=feedback['contact_name']
            user_email=feedback['contact_email']
            subject=f"{user_name} has asked about quote!"
            content=feedback['content']
            send_mail(
            subject,
            content,
            user_email,
            ["revadibrunda@gmail.com","pratikram.design@gmail.com","rebelupproduction@gmail.com"],
            fail_silently=False,
            connection=connection
        )
            form.clean()

class DetailViewsProject(DetailView):
    template_name="project_detail.html"
        
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = ContactForm()
    #     print(context['form'])
    #     return context

    # def post(self, request, *args, **kwargs):
        
    

    def get_context_data(self, **kwargs):
        context = super(Projects, self).get_context_data(**kwargs)
        context['item'] = Projects
        # form = ContactForm()
        # context['form']= form
        # print(form)
        return context
    
from django.core.mail import send_mail
from django.core import mail

connection = mail.get_connection()  # Use default email connection

def getQuote(request):
    # form = ContactForm(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print("FORM is valid")
        feedback = form.cleaned_data
        user_name=feedback['contact_name']
        user_email=feedback['contact_email']
        subject=f"{user_name} has asked about quote!"
        content=feedback['message']
        send_mail(
            subject,
            content,
            user_email,
            ["revadibrunda@gmail.com","pratikram.design@gmail.com","rebelupproduction@gmail.com"],
            fail_silently=False,
            connection=connection
        )
        form.clean()
        return redirect('Products_list')  # Replace 'success_url' with your URL name
    else:
        print(form.errors.as_data()) # here you print errors to terminal
    return render(request,'project_detail_quote.html',{'form':form})

















# # Create your views here.
# def products(request):

#     # Tileproducts.objects.create(tileName = "Black Forest Granite", description ="Black Forest Granite is a stunning natural stone featuring a dark, rich black base adorned with intricate veins of white, gray, and sometimes hints of deep red, reminiscent of the dense forests it's named after. Its elegant appearance makes it a popular choice for luxurious countertops, flooring, and accent pieces in interior design.", cost = 0,typeoftile="Granite",lenghtoftile="3cm",image="../static/Media/browntile.png")


#     # Getting all the stuff from database
#     query_results = Tileproducts.objects.all()

#     # Creating a dictionary to pass as an argument
#     contextcontent = { 'query_results' : query_results }
#     return render(request,template_name="products.html", context=contextcontent)


def project_detail(request):
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
            ["revadibrunda@gmail.com","pratikram.design@gmail.com","rebelupproduction@gmail.com"],
            fail_silently=False,
            connection=connection
        )
            form.clean()
            
            

    contextcontent = {'form': form}
    # Projects.objects.create(ProjectName = "Swiss Grey Marble", description ="Black Forest Granite is a stunning natural stone featuring a dark, rich black base adorned with intricate veins of white, gray, and sometimes hints of deep red, reminiscent of the dense forests it's named after. Its elegant appearance makes it a popular choice for luxurious countertops, flooring, and accent pieces in interior design.",image="{%static './Media/browntile.png'%}")
    return render(request,template_name="product_detail.html", context=contextcontent)