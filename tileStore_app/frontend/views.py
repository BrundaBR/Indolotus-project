from django.shortcuts import render
from backend.models import Tileproducts,Projects
# Create your views here.

def homePage(request):
    

    # Creating a dictionary to pass as an argument
    query_results=Tileproducts.objects.all()
    query_results2=Projects.objects.all()
    contextcontent = { 'query_results' : query_results, 'query2':query_results2 }
    return render(request,template_name="homePage.html",context=contextcontent)


def aboutPage(request):
    return render(request,template_name="aboutPage.html")


def contactPage(request):
    return render(request,template_name="contactPage.html")