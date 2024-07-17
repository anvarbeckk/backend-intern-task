from rest_framework import generics, permissions
from .models import User, Player, Tournament, Match
from .serializers import UserSerializer, PlayerSerializer, TournamentSerializer, MatchSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PlayerListView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TournamentListView(generics.ListCreateAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TournamentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class MatchListView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


from django.db.models import Sum


class LeaderboardView(generics.ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        tournament_id = self.kwargs['tournament_id']
        tournament = Tournament.objects.get(id=tournament_id)
        players = tournament.participants.all()
        leaderboard = players.annotate(total_points=Sum('match__result'))
        return leaderboard.order_by('-total_points')