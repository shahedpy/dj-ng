from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import views

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename='todo')

urlpatterns = [
    path('', views.index, name='index'),  # Frontend
    path('api/', include(router.urls)),
    path('api/auth/register/', views.create_user, name='register'),
    path('api/auth/login/', views.login_user, name='login'),
]
