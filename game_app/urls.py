from django.urls import path
from . import views
    
urlpatterns = [
    path('quiz/', views.play_quiz, name='play_quiz'),
]