from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('anleitungerstellen', views.AnleitungerstellenCreateView.as_view(), name='anleitungerstellen_add_page_create_view'),
    path('anleitungsschritteerstellen', views.AnleitungsschritterstellenCreateView.as_view(), name='anleitungsschritteerstellen_add_page_create_view'),

    path('anleitungdurchgehen/<int:pk>', views.AnleitungdurchgehenDetailView.as_view(), name='anleitungdurchgehen_detail_view'),
    path('anleitungfertig', views.AnleitungfertigDetailView.as_view(), name='anleitungfertig_detail_view'),
    
    path('profilerstellen', views.ProfilerstellenCreateView.as_view(), name='profilerstellen_create_view'),
    path('profileinloggen', views.ProfileinloggenDetailView.as_view(), name='profileinloggen_detail_view'),
    path('profileigeneanleitungen', views.ProfileigeneAnleitungenDetailView.as_view(), name='profileigeneAnleitungen_detail_view'),

]
urlpatterns += staticfiles_urlpatterns()

