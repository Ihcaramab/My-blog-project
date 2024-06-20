from django.urls import path
from .views import homepage, aboutpage, productpage, bloggpage, contactuspage
from . import views

# from .views import homepage
# urlpatterns = [
#     path("", homepage, name = "homepage"),
# ]

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("about", views.aboutpage, name = "aboutpage"),
    path("product", views.productpage, name = "productpage"),
    path("blogg", views.bloggpage, name = "bloggpage"),
    path("contactus", views.contactuspage, name = "contactuspage")

]
