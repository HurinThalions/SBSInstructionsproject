from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [

    path('anleitungerstellenaddpage', views.AnleitungerstellenAddPageCreateView.as_view(), name='anleitungerstellen_add_page_create_view'),

    path('anleitungdurchgehen/<int:pk>', views.AnleitungdurchgehenDetailView.as_view(), name='anleitungdurchgehen_detail_view'),
    path('anleitungfertig', views.AnleitungfertigDetailView.as_view(), name='anleitungfertig_detail_view'),
    
]
urlpatterns += staticfiles_urlpatterns()

