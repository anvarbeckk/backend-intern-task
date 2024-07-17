from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterView, PlayerListView, PlayerDetailView, TournamentListView, TournamentDetailView, MatchListView, MatchDetailView, LeaderboardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    path('tournaments/', TournamentListView.as_view(), name='tournament-list'),
    path('tournaments/<int:pk>', TournamentDetailView.as_view(), name='tournament-detail'),
    path('matches/', MatchListView.as_view(), name='match-list'),
    path('matches/<int:pk>', MatchDetailView.as_view(), name='match-detail'),
    path('tournaments/<int:tournament_id>/leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
]