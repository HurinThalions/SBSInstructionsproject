from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [

    path('anleitungerstellen/<int:pk>/', views.AnleitungerstellenDetailView.as_view(), name='anleitungerstellen_detail_view'),
    

    path('anleitungdurchgehen/<int:pk>', views.AnleitungdurchgehenDetailView.as_view(), name='anleitungdurchgehen_detail_view'),
    
]
urlpatterns += staticfiles_urlpatterns()

