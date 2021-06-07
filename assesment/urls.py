from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('addquestion', addquestion, name='addquestion'),
    path('createexam', createexam, name='createexam'),
    path('pendingexams', pendingexam, name='pendingexams'),
    path('previousexams', previousexam, name='previousexams'),
    path('attendpaper/<int:pk>', attendexam, name='attendpaper'),
    path('ongoingexams', ongoingexam, name='ongoingexams'),
    path('finishexam/<int:pk>', finishexam, name='finishexam'),
    path('completedexams', allcompletedexams, name='completedexams'),
]