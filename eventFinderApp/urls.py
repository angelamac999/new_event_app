from django.urls import path

from . import views


app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    path('create/', views.EventCreate.as_view(), name='create'),
    # event-finder/my-account
    path('my-account/', views.account, name='account'),
]
