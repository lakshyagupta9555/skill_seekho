from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse_skills, name='browse_skills'),
    path('matches/', views.my_matches, name='my_matches'),
    path('match/send/<int:skill_id>/', views.send_match_request, name='send_match'),
    path('match/accept/<int:match_id>/', views.accept_match, name='accept_match'),
    path('match/reject/<int:match_id>/', views.reject_match, name='reject_match'),
]
