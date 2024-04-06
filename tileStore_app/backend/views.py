from django.shortcuts import render
from .models import Tileproducts,Projects
from django.views.generic import ListView,DetailView




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




class DetailViewsProject(DetailView):
    model=Projects
    template_name="project_detail.html"
    context_object_name='item'

















# # Create your views here.
# def products(request):

#     # Tileproducts.objects.create(tileName = "Black Forest Granite", description ="Black Forest Granite is a stunning natural stone featuring a dark, rich black base adorned with intricate veins of white, gray, and sometimes hints of deep red, reminiscent of the dense forests it's named after. Its elegant appearance makes it a popular choice for luxurious countertops, flooring, and accent pieces in interior design.", cost = 0,typeoftile="Granite",lenghtoftile="3cm",image="../static/Media/browntile.png")


#     # Getting all the stuff from database
#     query_results = Tileproducts.objects.all()

#     # Creating a dictionary to pass as an argument
#     contextcontent = { 'query_results' : query_results }
#     return render(request,template_name="products.html", context=contextcontent)



# def projects(request):
#     # Projects.objects.create(ProjectName = "Swiss Grey Marble", description ="Black Forest Granite is a stunning natural stone featuring a dark, rich black base adorned with intricate veins of white, gray, and sometimes hints of deep red, reminiscent of the dense forests it's named after. Its elegant appearance makes it a popular choice for luxurious countertops, flooring, and accent pieces in interior design.",image="{%static './Media/browntile.png'%}")
    

#     # Getting all the stuff from database
#     query_results = Tileproducts.objects.all()

#     # Creating a dictionary to pass as an argument
#     context = { 'query_results' : query_results }
#     return render(request,template_name="projects.html", context=context)