"""
Complete Django Skill Swap Platform Setup Script
This script creates all necessary files and directories
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Directory structure
DIRECTORIES = [
    'skill_swap',
    'users/templates/users',
    'users/static/users/css',
    'users/static/users/js',
    'users/migrations',
    'dashboard/templates/dashboard',
    'dashboard/static/dashboard/css',
    'dashboard/static/dashboard/js',
    'dashboard/migrations',
    'chat/templates/chat',
    'chat/static/chat/css',
    'chat/static/chat/js',
    'chat/migrations',
    'video/templates/video',
    'video/static/video/css',
    'video/static/video/js',
    'video/migrations',
    'static/css',
    'static/js',
    'media/profile_pics',
    'media/skill_images',
    'templates',
]

# File contents dictionary
FILES = {
    # Main Project Files
    'skill_swap/__init__.py': '',
    
    'skill_swap/settings.py': '''"""
Django settings for skill_swap project.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-your-secret-key-change-in-production-12345678'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'users',
    'dashboard',
    'chat',
    'video',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'skill_swap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'skill_swap.wsgi.application'
ASGI_APPLICATION = 'skill_swap.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'dashboard:home'
LOGIN_URL = 'users:login'
LOGOUT_REDIRECT_URL = 'users:login'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
''',

    'skill_swap/urls.py': '''"""
Main URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('chat/', include('chat.urls')),
    path('video/', include('video.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
''',

    'skill_swap/asgi.py': '''"""
ASGI config for skill_swap project.
"""
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skill_swap.settings')

django_asgi_app = get_asgi_application()

from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        )
    ),
})
''',

    'skill_swap/wsgi.py': '''"""
WSGI config for skill_swap project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skill_swap.settings')

application = get_wsgi_application()
''',

    # Users App
    'users/__init__.py': '',
    'users/migrations/__init__.py': '',
    
    'users/apps.py': '''from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
''',

    'users/models.py': '''from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_picture:
            try:
                img = Image.open(self.profile_picture.path)
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.profile_picture.path)
            except:
                pass

class Skill(models.Model):
    SKILL_TYPES = (
        ('technical', 'Technical'),
        ('non_technical', 'Non-Technical'),
    )
    
    SKILL_LEVELS = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES)
    level = models.CharField(max_length=20, choices=SKILL_LEVELS)
    description = models.TextField()
    can_teach = models.BooleanField(default=False)
    want_to_learn = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.user.username}'

    class Meta:
        ordering = ['-created_at']
''',

    'users/signals.py': '''from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
''',

    'users/admin.py': '''from django.contrib import admin
from .models import Profile, Skill

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'created_at']
    search_fields = ['user__username', 'location']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'skill_type', 'level', 'can_teach', 'want_to_learn']
    list_filter = ['skill_type', 'level', 'can_teach', 'want_to_learn']
    search_fields = ['name', 'user__username']
''',

    'users/forms.py': '''from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'location', 'phone', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'skill_type', 'level', 'description', 'can_teach', 'want_to_learn']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
''',

    'users/views.py': '''from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, SkillForm
from .models import Skill

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('dashboard:home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

@login_required
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, 'Skill added successfully!')
            return redirect('users:profile')
    else:
        form = SkillForm()
    return render(request, 'users/add_skill.html', {'form': form})

@login_required
def delete_skill(request, pk):
    skill = Skill.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully!')
        return redirect('users:profile')
    return render(request, 'users/delete_skill.html', {'skill': skill})
''',

    'users/urls.py': '''from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('delete-skill/<int:pk>/', views.delete_skill, name='delete_skill'),
]
''',

    # Dashboard App
    'dashboard/__init__.py': '',
    'dashboard/migrations/__init__.py': '',
    
    'dashboard/apps.py': '''from django.apps import AppConfig

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
''',

    'dashboard/models.py': '''from django.db import models
from django.contrib.auth.models import User
from users.models import Skill

class SkillMatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_sent')
    matched_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_received')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ), default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} -> {self.matched_user.username} ({self.skill.name})'

    class Meta:
        ordering = ['-created_at']
''',

    'dashboard/admin.py': '''from django.contrib import admin
from .models import SkillMatch

@admin.register(SkillMatch)
class SkillMatchAdmin(admin.ModelAdmin):
    list_display = ['user', 'matched_user', 'skill', 'status', 'created_at']
    list_filter = ['status', 'created_at']
''',

    'dashboard/views.py': '''from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from users.models import Skill
from .models import SkillMatch

@login_required
def home(request):
    my_skills = Skill.objects.filter(user=request.user)
    
    # Find matching skills
    teach_skills = my_skills.filter(can_teach=True)
    learn_skills = my_skills.filter(want_to_learn=True)
    
    # Get potential matches
    potential_matches = Skill.objects.filter(
        Q(can_teach=True, name__in=learn_skills.values_list('name', flat=True)) |
        Q(want_to_learn=True, name__in=teach_skills.values_list('name', flat=True))
    ).exclude(user=request.user).select_related('user')[:10]
    
    context = {
        'my_skills': my_skills,
        'potential_matches': potential_matches,
    }
    return render(request, 'dashboard/home.html', context)

@login_required
def browse_skills(request):
    skill_type = request.GET.get('type', '')
    search = request.GET.get('search', '')
    
    skills = Skill.objects.exclude(user=request.user).select_related('user')
    
    if skill_type:
        skills = skills.filter(skill_type=skill_type)
    if search:
        skills = skills.filter(Q(name__icontains=search) | Q(description__icontains=search))
    
    context = {
        'skills': skills,
        'skill_type': skill_type,
        'search': search,
    }
    return render(request, 'dashboard/browse_skills.html', context)

@login_required
def send_match_request(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    if skill.user == request.user:
        messages.error(request, 'Cannot send match request to yourself!')
        return redirect('dashboard:home')
    
    # Check if already sent
    existing = SkillMatch.objects.filter(user=request.user, matched_user=skill.user, skill=skill).exists()
    if existing:
        messages.info(request, 'Match request already sent!')
    else:
        SkillMatch.objects.create(user=request.user, matched_user=skill.user, skill=skill)
        messages.success(request, 'Match request sent!')
    
    return redirect('dashboard:browse_skills')

@login_required
def my_matches(request):
    sent = SkillMatch.objects.filter(user=request.user).select_related('matched_user', 'skill')
    received = SkillMatch.objects.filter(matched_user=request.user).select_related('user', 'skill')
    
    context = {
        'sent_matches': sent,
        'received_matches': received,
    }
    return render(request, 'dashboard/my_matches.html', context)

@login_required
def accept_match(request, match_id):
    match = get_object_or_404(SkillMatch, id=match_id, matched_user=request.user)
    match.status = 'accepted'
    match.save()
    messages.success(request, 'Match accepted! You can now chat.')
    return redirect('dashboard:my_matches')

@login_required
def reject_match(request, match_id):
    match = get_object_or_404(SkillMatch, id=match_id, matched_user=request.user)
    match.status = 'rejected'
    match.save()
    messages.info(request, 'Match rejected.')
    return redirect('dashboard:my_matches')
''',

    'dashboard/urls.py': '''from django.urls import path
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
''',

    # Chat App
    'chat/__init__.py': '',
    'chat/migrations/__init__.py': '',
    
    'chat/apps.py': '''from django.apps import AppConfig

class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
''',

    'chat/models.py': '''from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    participants = models.ManyToManyField(User, related_name='chat_rooms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender.username}: {self.content[:50]}'

    class Meta:
        ordering = ['timestamp']
''',

    'chat/admin.py': '''from django.contrib import admin
from .models import ChatRoom, Message

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'room', 'content', 'timestamp']
    list_filter = ['timestamp']
''',

    'chat/views.py': '''from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import ChatRoom, Message

@login_required
def chat_list(request):
    rooms = request.user.chat_rooms.all()
    return render(request, 'chat/chat_list.html', {'rooms': rooms})

@login_required
def chat_room(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name, participants=request.user)
    messages = room.messages.all().select_related('sender')
    
    # Mark messages as read
    Message.objects.filter(room=room).exclude(sender=request.user).update(is_read=True)
    
    # Get other participant
    other_user = room.participants.exclude(id=request.user.id).first()
    
    context = {
        'room': room,
        'messages': messages,
        'other_user': other_user,
    }
    return render(request, 'chat/chat_room.html', context)

@login_required
def start_chat(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    if other_user == request.user:
        return redirect('chat:chat_list')
    
    # Create or get room name
    users_sorted = sorted([request.user.id, other_user.id])
    room_name = f'chat_{users_sorted[0]}_{users_sorted[1]}'
    
    room, created = ChatRoom.objects.get_or_create(name=room_name)
    if created:
        room.participants.add(request.user, other_user)
    
    return redirect('chat:chat_room', room_name=room_name)
''',

    'chat/urls.py': '''from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('room/<str:room_name>/', views.chat_room, name='chat_room'),
    path('start/<int:user_id>/', views.start_chat, name='start_chat'),
]
''',

    'chat/routing.py': '''from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\\w+)/$', consumers.ChatConsumer.as_asgi()),
]
''',

    'chat/consumers.py': '''import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import ChatRoom, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        
        await self.save_message(username, self.room_name, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username']
        }))

    @database_sync_to_async
    def save_message(self, username, room_name, message):
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(name=room_name)
        Message.objects.create(sender=user, room=room, content=message)
''',

    # Video App
    'video/__init__.py': '',
    'video/migrations/__init__.py': '',
    
    'video/apps.py': '''from django.apps import AppConfig

class VideoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video'
''',

    'video/models.py': '''from django.db import models
from django.contrib.auth.models import User

class VideoCall(models.Model):
    caller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calls_made')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calls_received')
    room_id = models.CharField(max_length=255, unique=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(default=0, help_text='Duration in seconds')
    status = models.CharField(max_length=20, choices=(
        ('calling', 'Calling'),
        ('active', 'Active'),
        ('ended', 'Ended'),
        ('missed', 'Missed'),
    ), default='calling')

    def __str__(self):
        return f'{self.caller.username} -> {self.receiver.username} ({self.status})'

    class Meta:
        ordering = ['-started_at']
''',

    'video/admin.py': '''from django.contrib import admin
from .models import VideoCall

@admin.register(VideoCall)
class VideoCallAdmin(admin.ModelAdmin):
    list_display = ['caller', 'receiver', 'status', 'started_at', 'duration']
    list_filter = ['status', 'started_at']
''',

    'video/views.py': '''from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import VideoCall
import uuid

@login_required
def video_call_list(request):
    calls = VideoCall.objects.filter(
        models.Q(caller=request.user) | models.Q(receiver=request.user)
    ).order_by('-started_at')[:20]
    return render(request, 'video/call_list.html', {'calls': calls})

@login_required
def start_call(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    if receiver == request.user:
        return redirect('dashboard:home')
    
    room_id = str(uuid.uuid4())
    call = VideoCall.objects.create(
        caller=request.user,
        receiver=receiver,
        room_id=room_id,
        status='calling'
    )
    
    return redirect('video:video_room', room_id=room_id)

@login_required
def video_room(request, room_id):
    call = get_object_or_404(VideoCall, room_id=room_id)
    
    # Check if user is participant
    if call.caller != request.user and call.receiver != request.user:
        return redirect('dashboard:home')
    
    if call.status == 'calling':
        call.status = 'active'
        call.save()
    
    context = {
        'call': call,
        'room_id': room_id,
    }
    return render(request, 'video/video_room.html', context)
''',

    'video/urls.py': '''from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.video_call_list, name='call_list'),
    path('start/<int:user_id>/', views.start_call, name='start_call'),
    path('room/<str:room_id>/', views.video_room, name='video_room'),
]
''',
}

def create_structure():
    """Create all directories and files"""
    
    # Create directories
    print("Creating directory structure...")
    for directory in DIRECTORIES:
        dir_path = BASE_DIR / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {directory}")
    
    # Create files
    print("\\nCreating project files...")
    for file_path, content in FILES.items():
        full_path = BASE_DIR / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {file_path}")
    
    print("\\n✅ Project structure created successfully!")
    print("\\nNext steps:")
    print("1. Activate virtual environment: venv\\Scripts\\activate")
    print("2. Install dependencies: pip install django djangorestframework channels daphne pillow")
    print("3. Run migrations: python manage.py makemigrations && python manage.py migrate")
    print("4. Create superuser: python manage.py createsuperuser")
    print("5. Run server: python manage.py runserver")

if __name__ == '__main__':
    create_structure()
