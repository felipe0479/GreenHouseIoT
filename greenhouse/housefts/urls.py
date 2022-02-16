from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('statics', views.plot, name='plot'),
    path('create',views.saveEnv,name="CreateEnv"),
    path('search/',views.date_plot,name='search plot')
]