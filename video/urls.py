from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.video_call_list, name='call_list'),
    path('start/<int:user_id>/', views.start_call, name='start_call'),
    path('room/<str:room_id>/', views.video_room, name='video_room'),
]
