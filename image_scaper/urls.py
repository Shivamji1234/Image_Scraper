from django.urls import path
from .views import home_page,image_scrap

urlpatterns = [
    path('search/',home_page,name="home_page"),
    path("search/comment/",image_scrap,name="image_scrap")
]