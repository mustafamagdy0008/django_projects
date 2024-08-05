from django.urls import path
from . import views

urlpatterns = [
    path('game/<slug:guess>', views.GameView.as_view()),
    path('simple/', views.Simple.as_view()),
    path('guess/<slug:zap>', views.Guess.as_view()),
 ]
