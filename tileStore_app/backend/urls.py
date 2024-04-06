from django.urls import path,include
# from .views import products
from .views import HomeView,DetailViews,HomeViewProject,DetailViewsProject
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("view/<int:pk>/",DetailViews.as_view(),name="products-detail"),
    path("view/",HomeView.as_view(),name="products-list"),
    path("view/projects/<int:pk>/",DetailViewsProject.as_view(),name="project-detail"),
    path("view/projects/",HomeViewProject.as_view(),name="project-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)