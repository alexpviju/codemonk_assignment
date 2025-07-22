from django.urls import path
from .views import RegisterView, LoginView,ParagraphUploadView,WordSearchView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('paragraphs/', ParagraphUploadView.as_view(), name='upload_paragraphs'),
    path('search/', WordSearchView.as_view(), name='search_word'),
]