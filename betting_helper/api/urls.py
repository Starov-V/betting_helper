from django.urls import include, path

from rest_framework import routers
from .views import BetViewSet


v1_router = routers.DefaultRouter()
v1_router.register(
    r'bet',
    BetViewSet,
    basename='bets'
)

urlpatterns = [
    path(r'v1/bet/update/', BetViewSet.as_view({'get':'calculate'})),
    path('v1/', include(v1_router.urls)),
]