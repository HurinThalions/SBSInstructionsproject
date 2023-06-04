from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path


from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('anleitungerstellen', views.AnleitungerstellenCreateView.as_view(), name='anleitungerstellen_add_page_create_view'),
    path('anleitungsschritteerstellen', views.AnleitungsschritterstellenCreateView.as_view(), name='anleitungsschritteerstellen_add_page_create_view'),
    path('komponentenerstellen', views.KomponentenerstellenCreateView.as_view(), name='komponentenerstellen_createview'),

    path('anleitungdurchgehen/<int:pk>', views.AnleitungdurchgehenDetailView.as_view(), name='anleitungdurchgehen_detail_view'),
    
    path('profilerstellen', views.ProfilerstellenCreateView.as_view(), name='profilerstellen_create_view'),
    path('login', views.ProfileinloggenLoginView.as_view(), name='Profileinloggen_login_view'),
    path('profileigeneanleitungen/<int:pk>', views.ProfileigeneAnleitungenDetailView.as_view(), name='profileigeneanleitungen'),

    path('anleitungfertig', views.anleitungfertig, name='anleitungfertig'),
    path('entwurffertig', views.entwurffertig, name='entwurffertig'),
    path('anleitunggespeichert', views.anleitunggespeichert, name='anleitunggespeichert'),

    # path('', views.KatalogDetailView.as_view(), name='katalog_detail_view'),
    
]
urlpatterns += staticfiles_urlpatterns()

