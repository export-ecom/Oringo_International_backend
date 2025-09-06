from django.urls import path
from .views import RegisterView
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from .views import MyTokenObtainPairView, MeView
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("me/", MeView.as_view(), name="me"),    

    # path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("logout/", TokenBlacklistView.as_view(), name="logout"),
]
