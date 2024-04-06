from django.urls import path,include
from .views import homePage,aboutPage,contactPage
from backend.views import HomeView

urlpatterns = [
    path("",homePage,name="Home"),
    path("about/",aboutPage,name="About"),
    path("contact/",contactPage,name="Contact"),
    path("stone-catalog/",HomeView.as_view(),name="Products_list"),
]
