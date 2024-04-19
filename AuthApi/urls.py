from django.urls import path, include
from .views import AccountUserViewSet, AccountTokenDestroyView, AccountUserDeleteView

urlpatterns = [
    path('users/', AccountUserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('delete/<int:user_id>/', AccountUserDeleteView.as_view(), name='user-delete'),
    path('token/destroy/', AccountTokenDestroyView.as_view(), name='token-destroy'),
]