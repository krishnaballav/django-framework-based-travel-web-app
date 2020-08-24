from django.urls import path

from . import views

urlpatterns = [path("register", views.register , name="register"),
               path("login" , views.login, name="login"),
                 path("logout" , views.logout, name="logout"),
                  path("goa" , views.goa, name="goa"),
                   path("photos" , views.photos, name="photos"),
                    path("userindex" , views.userindex, name="userindex"),


]