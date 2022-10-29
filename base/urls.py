from django.urls import path,include
from .views import *


urlpatterns = [

   # path('', index, name = 'index'),
   path('', homepage, name = 'homepage'),
   path('event/<int:pk>', eventpage, name = 'event_page'),
   path('registration-confirmaton/<int:pk>', registration_confirmation, name = 'registration_confirmaton'), 
   path('profile/<int:pk>', profile, name = 'profile'),
   path('account/', account, name = 'account'),
   path('project-submission/<int:pk>', project_submission, name = 'psubmission'),


]