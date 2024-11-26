from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('destinations/', views.destinations, name="destinations"),
    path('destination/<int:pk>', views.DestinationDetailView.as_view(), name="destinations"),
    path('cruise/', views.cruises, name="cruises"),
    path('cruise/<int:pk>', views.CruiseDetailView.as_view(), name="destinations"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('reset-password/', views.reset_password, name="reset_password"),
]
