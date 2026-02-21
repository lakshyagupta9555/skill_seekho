"""
Create all HTML templates for Skill Swap Platform
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

TEMPLATES = {
    'templates/base.html': '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Skill Swap{% endblock %}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        dark: {
                            bg: '#0f172a',
                            card: '#1e293b',
                            border: '#334155',
                        }
                    }
                }
            }
        }
    </script>
    {% block extra_css %}{% endblock %}
</head>
<body class="bg-dark-bg text-gray-100 min-h-screen">
    <!-- Navigation -->
    <nav class="bg-dark-card border-b border-dark-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16">
                <div class="flex">
                    <div class="flex-shrink-0 flex items-center">
                        <a href="{% url 'dashboard:home' %}" class="text-2xl font-bold text-blue-400">SkillSwap</a>
                    </div>
                    {% if user.is_authenticated %}
                    <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
                        <a href="{% url 'dashboard:home' %}" class="inline-flex items-center px-1 pt-1 text-gray-300 hover:text-white">Dashboard</a>
                        <a href="{% url 'dashboard:browse_skills' %}" class="inline-flex items-center px-1 pt-1 text-gray-300 hover:text-white">Browse Skills</a>
                        <a href="{% url 'dashboard:my_matches' %}" class="inline-flex items-center px-1 pt-1 text-gray-300 hover:text-white">My Matches</a>
                        <a href="{% url 'chat:chat_list' %}" class="inline-flex items-center px-1 pt-1 text-gray-300 hover:text-white">Chat</a>
                        <a href="{% url 'video:call_list' %}" class="inline-flex items-center px-1 pt-1 text-gray-300 hover:text-white">Video</a>
                    </div>
                    {% endif %}
                </div>
                <div class="flex items-center">
                    {% if user.is_authenticated %}
                    <div class="ml-3 relative flex items-center space-x-4">
                        <a href="{% url 'users:profile' %}" class="text-gray-300 hover:text-white">{{ user.username }}</a>
                        <a href="{% url 'users:logout' %}" class="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm">Logout</a>
                    </div>
                    {% else %}
                    <div class="space-x-4">
                        <a href="{% url 'users:login' %}" class="text-gray-300 hover:text-white">Login</a>
                        <a href="{% url 'users:register' %}" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm">Register</a>
                    </div>
                    {% endif %}
                </div>
            </div>
        </div>
    </nav>

    <!-- Messages -->
    {% if messages %}
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-4">
        {% for message in messages %}
        <div class="bg-{% if message.tags == 'error' %}red{% elif message.tags == 'success' %}green{% else %}blue{% endif %}-900 border border-{% if message.tags == 'error' %}red{% elif message.tags == 'success' %}green{% else %}blue{% endif %}-700 text-white px-4 py-3 rounded mb-4">
            {{ message }}
        </div>
        {% endfor %}
    </div>
    {% endif %}

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {% block content %}{% endblock %}
    </main>

    {% block extra_js %}{% endblock %}
</body>
</html>''',

    'users/templates/users/login.html': '''{% extends 'base.html' %}

{% block title %}Login - Skill Swap{% endblock %}

{% block content %}
<div class="max-w-md mx-auto">
    <div class="bg-dark-card rounded-lg shadow-xl p-8 border border-dark-border">
        <h2 class="text-3xl font-bold text-center mb-8 text-blue-400">Login to SkillSwap</h2>
        
        <form method="post" class="space-y-6">
            {% csrf_token %}
            
            <div>
                <label for="id_username" class="block text-sm font-medium text-gray-300">Username</label>
                <input type="text" name="username" id="id_username" required 
                       class="mt-1 block w-full bg-dark-bg border border-dark-border rounded-md px-3 py-2 text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            
            <div>
                <label for="id_password" class="block text-sm font-medium text-gray-300">Password</label>
                <input type="password" name="password" id="id_password" required 
                       class="mt-1 block w-full bg-dark-bg border border-dark-border rounded-md px-3 py-2 text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            
            <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md transition duration-200">
                Login
            </button>
        </form>
        
        <div class="mt-6 text-center">
            <p class="text-gray-400">Don't have an account? 
                <a href="{% url 'users:register' %}" class="text-blue-400 hover:text-blue-300">Register here</a>
            </p>
        </div>
    </div>
</div>
{% endblock %}''',

    'users/templates/users/register.html': '''{% extends 'base.html' %}

{% block title %}Register - Skill Swap{% endblock %}

{% block content %}
<div class="max-w-md mx-auto">
    <div class="bg-dark-card rounded-lg shadow-xl p-8 border border-dark-border">
        <h2 class="text-3xl font-bold text-center mb-8 text-blue-400">Join SkillSwap</h2>
        
        <form method="post" class="space-y-4">
            {% csrf_token %}
            
            {% for field in form %}
            <div>
                <label for="{{ field.id_for_label }}" class="block text-sm font-medium text-gray-300">
                    {{ field.label }}
                </label>
                <input type="{{ field.field.widget.input_type }}" 
                       name="{{ field.name }}" 
                       id="{{ field.id_for_label }}"
                       {% if field.field.required %}required{% endif %}
                       class="mt-1 block w-full bg-dark-bg border border-dark-border rounded-md px-3 py-2 text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500">
                {% if field.errors %}
                    <p class="mt-1 text-sm text-red-400">{{ field.errors.0 }}</p>
                {% endif %}
                {% if field.help_text %}
                    <p class="mt-1 text-xs text-gray-400">{{ field.help_text }}</p>
                {% endif %}
            </div>
            {% endfor %}
            
            <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md transition duration-200">
                Register
            </button>
        </form>
        
        <div class="mt-6 text-center">
            <p class="text-gray-400">Already have an account? 
                <a href="{% url 'users:login' %}" class="text-blue-400 hover:text-blue-300">Login here</a>
            </p>
        </div>
    </div>
</div>
{% endblock %}''',

    'users/templates/users/profile.html': '''{% extends 'base.html' %}

{% block title %}Profile - Skill Swap{% endblock %}

{% block content %}
<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <!-- Profile Info -->
    <div class="bg-dark-card rounded-lg shadow-xl p-6 border border-dark-border">
        <h2 class="text-2xl font-bold mb-6 text-blue-400">Update Profile</h2>
        
        <form method="post" enctype="multipart/form-data" class="space-y-4">
            {% csrf_token %}
            
            <div class="text-center mb-4">
                {% if user.profile.profile_picture %}
                <img src="{{ user.profile.profile_picture.url }}" alt="Profile" class="w-32 h-32 rounded-full mx-auto border-4 border-blue-500">
                {% endif %}
            </div>
            
            {% for field in u_form %}
            <div>
                <label class="block text-sm font-medium text-gray-300">{{ field.label }}</label>
                {{ field }}
            </div>
            {% endfor %}
            
            {% for field in p_form %}
            <div>
                <label class="block text-sm font-medium text-gray-300">{{ field.label }}</label>
                {{ field }}
            </div>
            {% endfor %}
            
            <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md">
                Update Profile
            </button>
        </form>
    </div>
    
    <!-- My Skills -->
    <div class="bg-dark-card rounded-lg shadow-xl p-6 border border-dark-border">
        <div class="flex justify-between items-center mb-6">
            <h2 class="text-2xl font-bold text-blue-400">My Skills</h2>
            <a href="{% url 'users:add_skill' %}" class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-md text-sm">
                Add Skill
            </a>
        </div>
        
        <div class="space-y-4">
            {% for skill in user.skills.all %}
            <div class="bg-dark-bg border border-dark-border rounded-lg p-4">
                <div class="flex justify-between items-start">
                    <div>
                        <h3 class="text-lg font-semibold text-white">{{ skill.name }}</h3>
                        <p class="text-sm text-gray-400">{{ skill.get_skill_type_display }} - {{ skill.get_level_display }}</p>
                        <p class="text-sm text-gray-300 mt-2">{{ skill.description }}</p>
                        <div class="mt-2 space-x-2">
                            {% if skill.can_teach %}
                            <span class="inline-block bg-green-900 text-green-200 text-xs px-2 py-1 rounded">Can Teach</span>
                            {% endif %}
                            {% if skill.want_to_learn %}
                            <span class="inline-block bg-blue-900 text-blue-200 text-xs px-2 py-1 rounded">Want to Learn</span>
                            {% endif %}
                        </div>
                    </div>
                    <form method="post" action="{% url 'users:delete_skill' skill.id %}">
                        {% csrf_token %}
                        <button type="submit" class="text-red-400 hover:text-red-300">Delete</button>
                    </form>
                </div>
            </div>
            {% empty %}
            <p class="text-gray-400 text-center py-8">No skills added yet.</p>
            {% endfor %}
        </div>
    </div>
</div>

<style>
    input, textarea, select {
        background-color: #0f172a;
        border: 1px solid #334155;
        color: #f1f5f9;
        padding: 0.5rem;
        border-radius: 0.375rem;
        width: 100%;
    }
    input:focus, textarea:focus, select:focus {
        outline: none;
        border-color: #3b82f6;
        ring: 2px;
        ring-color: #3b82f6;
    }
</style>
{% endblock %}''',

    'users/templates/users/add_skill.html': '''{% extends 'base.html' %}

{% block title %}Add Skill - Skill Swap{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto">
    <div class="bg-dark-card rounded-lg shadow-xl p-8 border border-dark-border">
        <h2 class="text-3xl font-bold mb-8 text-blue-400">Add New Skill</h2>
        
        <form method="post" class="space-y-4">
            {% csrf_token %}
            
            {% for field in form %}
            <div>
                <label for="{{ field.id_for_label }}" class="block text-sm font-medium text-gray-300 mb-2">
                    {{ field.label }}
                </label>
                {{ field }}
                {% if field.errors %}
                    <p class="mt-1 text-sm text-red-400">{{ field.errors.0 }}</p>
                {% endif %}
            </div>
            {% endfor %}
            
            <div class="flex space-x-4">
                <button type="submit" class="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md">
                    Add Skill
                </button>
                <a href="{% url 'users:profile' %}" class="flex-1 bg-gray-600 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded-md text-center">
                    Cancel
                </a>
            </div>
        </form>
    </div>
</div>

<style>
    input, textarea, select {
        background-color: #0f172a;
        border: 1px solid #334155;
        color: #f1f5f9;
        padding: 0.5rem;
        border-radius: 0.375rem;
        width: 100%;
    }
    input:focus, textarea:focus, select:focus {
        outline: none;
        border-color: #3b82f6;
    }
    input[type="checkbox"] {
        width: auto;
        margin-right: 0.5rem;
    }
</style>
{% endblock %}''',

    'users/templates/users/delete_skill.html': '''{% extends 'base.html' %}

{% block title %}Delete Skill - Skill Swap{% endblock %}

{% block content %}
<div class="max-w-md mx-auto">
    <div class="bg-dark-card rounded-lg shadow-xl p-8 border border-red-900">
        <h2 class="text-2xl font-bold mb-4 text-red-400">Confirm Deletion</h2>
        <p class="text-gray-300 mb-6">Are you sure you want to delete "{{ skill.name }}"?</p>
        
        <form method="post" class="space-y-4">
            {% csrf_token %}
            <div class="flex space-x-4">
                <button type="submit" class="flex-1 bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-md">
                    Delete
                </button>
                <a href="{% url 'users:profile' %}" class="flex-1 bg-gray-600 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded-md text-center">
                    Cancel
                </a>
            </div>
        </form>
    </div>
</div>
{% endblock %}''',

    'dashboard/templates/dashboard/home.html': '''{% extends 'base.html' %}

{% block title %}Dashboard - Skill Swap{% endblock %}

{% block content %}
<div class="space-y-8">
    <!-- Welcome Section -->
    <div class="bg-gradient-to-r from-blue-900 to-purple-900 rounded-lg shadow-xl p-8 border border-blue-800">
        <h1 class="text-4xl font-bold text-white mb-2">Welcome, {{ user.first_name|default:user.username }}!</h1>
        <p class="text-blue-200">Ready to share your skills and learn something new?</p>
    </div>

    <!-- Stats -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-dark-card rounded-lg shadow-xl p-6 border border-dark-border">
            <h3 class="text-gray-400 text-sm font-medium">My Skills</h3>
            <p class="text-3xl font-bold text-blue-400">{{ my_skills.count }}</p>
        </div>
        <div class="bg-dark-card rounded-lg shadow-xl p-6 border border-dark-border">
            <h3 class="text-gray-400 text-sm font-medium">Can Teach</h3>
            <p class="text-3xl font-bold text-green-400">{{ my_skills|length }}</p>
        </div>
        <div class="bg-dark-card rounded-lg shadow-xl p-6 border border-dark-border">
            <h3 class="text-gray-400 text-sm font-medium">Want to Learn</h3>
            <p class="text-3xl font-bold text-purple-400">{{ my_skills|length }}</p>
        </div>
    </div>

    <!-- Potential Matches -->
    <div class="bg-dark-card rounded-lg shadow-xl p-6 border border-dark-border">
        <h2 class="text-2xl font-bold mb-6 text-blue-400">Potential Matches</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            {% for skill in potential_matches %}
            <div class="bg-dark-bg border border-dark-border rounded-lg p-4 hover:border-blue-500 transition">
                <div class="flex items-start justify-between">
                    <div>
                        <h3 class="text-lg font-semibold text-white">{{ skill.name }}</h3>
                        <p class="text-sm text-gray-400">by {{ skill.user.username }}</p>
                        <p class="text-sm text-gray-300 mt-2">{{ skill.description|truncatewords:20 }}</p>
                        <div class="mt-2">
                            <span class="inline-block bg-blue-900 text-blue-200 text-xs px-2 py-1 rounded">
                                {{ skill.get_level_display }}
                            </span>
                        </div>
                    </div>
                    <div class="flex flex-col space-y-2">
                        <a href="{% url 'dashboard:send_match' skill.id %}" 
                           class="bg-blue-600 hover:bg-blue-700 text-white text-xs px-3 py-1 rounded">
                            Connect
                        </a>
                        <a href="{% url 'chat:start_chat' skill.user.id %}" 
                           class="bg-green-600 hover:bg-green-700 text-white text-xs px-3 py-1 rounded">
                            Chat
                        </a>
                    </div>
                </div>
            </div>
            {% empty %}
            <p class="text-gray-400 col-span-2 text-center py-8">No matches found. Add more skills to find matches!</p>
            {% endfor %}
        </div>
        
        <div class="mt-6 text-center">
            <a href="{% url 'dashboard:browse_skills' %}" class="text-blue-400 hover:text-blue-300">
                Browse all skills →
            </a>
        </div>
    </div>
</div>
{% endblock %}''',

    'dashboard/templates/dashboard/browse_skills.html': '''{% extends 'base.html' %}

{% block title %}Browse Skills - Skill Swap{% endblock %}

{% block content %}
<div class="space-y-6">
    <h1 class="text-3xl font-bold text-blue-400">Browse Skills</h1>
    
    <!-- Filters -->
    <div class="bg-dark-card rounded-lg shadow-xl p-6 border border-dark-border">
        <form method="get" class="flex flex-wrap gap-4">
            <div class="flex-1 min-w-64">
                <input type="text" name="search" value="{{ search }}" placeholder="Search skills..." 
                       class="w-full bg-dark-bg border border-dark-border rounded-md px-4 py-2 text-gray-100">
            </div>
            <select name="type" class="bg-dark-bg border border-dark-border rounded-md px-4 py-2 text-gray-100">
                <option value="">All Types</option>
                <option value="technical" {% if skill_type == 'technical' %}selected{% endif %}>Technical</option>
                <option value="non_technical" {% if skill_type == 'non_technical' %}selected{% endif %}>Non-Technical</option>
            </select>
            <button type="submit" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-md">
                Filter
            </button>
        </form>
    </div>
    
    <!-- Skills Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {% for skill in skills %}
        <div class="bg-dark-card rounded-lg shadow-xl p-6 border border-dark-border hover:border-blue-500 transition">
            <h3 class="text-xl font-bold text-white mb-2">{{ skill.name }}</h3>
            <p class="text-sm text-gray-400 mb-2">by {{ skill.user.username }}</p>
            <p class="text-sm text-gray-300 mb-4">{{ skill.description|truncatewords:15 }}</p>
            
            <div class="flex flex-wrap gap-2 mb-4">
                <span class="bg-blue-900 text-blue-200 text-xs px-2 py-1 rounded">
                    {{ skill.get_skill_type_display }}
                </span>
                <span class="bg-purple-900 text-purple-200 text-xs px-2 py-1 rounded">
                    {{ skill.get_level_display }}
                </span>
                {% if skill.can_teach %}
                <span class="bg-green-900 text-green-200 text-xs px-2 py-1 rounded">Can Teach</span>
                {% endif %}
            </div>
            
            <div class="flex space-x-2">
                <a href="{% url 'dashboard:send_match' skill.id %}" 
                   class="flex-1 bg-blue-600 hover:bg-blue-700 text-white text-center py-2 rounded-md text-sm">
                    Connect
                </a>
                <a href="{% url 'chat:start_chat' skill.user.id %}" 
                   class="flex-1 bg-green-600 hover:bg-green-700 text-white text-center py-2 rounded-md text-sm">
                    Chat
                </a>
            </div>
        </div>
        {% empty %}
        <p class="text-gray-400 col-span-3 text-center py-8">No skills found.</p>
        {% endfor %}
    </div>
</div>

<style>
    input, select {
        background-color: #0f172a;
        border: 1px solid #334155;
        color: #f1f5f9;
    }
    input:focus, select:focus {
        outline: none;
        border-color: #3b82f6;
    }
</style>
{% endblock %}''',

    'dashboard/templates/dashboard/my_matches.html': '''{% extends 'base.html' %}

{% block title %}My Matches - Skill Swap{% endblock %}

{% block content %}
<div class="space-y-8">
    <h1 class="text-3xl font-bold text-blue-400">My Matches</h1>
    
    <!-- Received Requests -->
    <div class="bg-dark-card rounded-lg shadow-xl p-6 border border-dark-border">
        <h2 class="text-2xl font-bold mb-4 text-green-400">Received Requests</h2>
        <div class="space-y-4">
            {% for match in received_matches %}
            <div class="bg-dark-bg border border-dark-border rounded-lg p-4">
                <div class="flex justify-between items-center">
                    <div>
                        <h3 class="text-lg font-semibold text-white">{{ match.user.username }}</h3>
                        <p class="text-sm text-gray-400">Skill: {{ match.skill.name }}</p>
                        <p class="text-sm text-gray-500">{{ match.created_at|date:"M d, Y" }}</p>
                        <span class="inline-block mt-2 text-xs px-2 py-1 rounded
                            {% if match.status == 'pending' %}bg-yellow-900 text-yellow-200
                            {% elif match.status == 'accepted' %}bg-green-900 text-green-200
                            {% else %}bg-red-900 text-red-200{% endif %}">
                            {{ match.get_status_display }}
                        </span>
                    </div>
                    {% if match.status == 'pending' %}
                    <div class="flex space-x-2">
                        <a href="{% url 'dashboard:accept_match' match.id %}" 
                           class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-md text-sm">
                            Accept
                        </a>
                        <a href="{% url 'dashboard:reject_match' match.id %}" 
                           class="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm">
                            Reject
                        </a>
                    </div>
                    {% elif match.status == 'accepted' %}
                    <a href="{% url 'chat:start_chat' match.user.id %}" 
                       class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm">
                        Start Chat
                    </a>
                    {% endif %}
                </div>
            </div>
            {% empty %}
            <p class="text-gray-400 text-center py-4">No received requests.</p>
            {% endfor %}
        </div>
    </div>
    
    <!-- Sent Requests -->
    <div class="bg-dark-card rounded-lg shadow-xl p-6 border border-dark-border">
        <h2 class="text-2xl font-bold mb-4 text-blue-400">Sent Requests</h2>
        <div class="space-y-4">
            {% for match in sent_matches %}
            <div class="bg-dark-bg border border-dark-border rounded-lg p-4">
                <div class="flex justify-between items-center">
                    <div>
                        <h3 class="text-lg font-semibold text-white">{{ match.matched_user.username }}</h3>
                        <p class="text-sm text-gray-400">Skill: {{ match.skill.name }}</p>
                        <p class="text-sm text-gray-500">{{ match.created_at|date:"M d, Y" }}</p>
                        <span class="inline-block mt-2 text-xs px-2 py-1 rounded
                            {% if match.status == 'pending' %}bg-yellow-900 text-yellow-200
                            {% elif match.status == 'accepted' %}bg-green-900 text-green-200
                            {% else %}bg-red-900 text-red-200{% endif %}">
                            {{ match.get_status_display }}
                        </span>
                    </div>
                    {% if match.status == 'accepted' %}
                    <a href="{% url 'chat:start_chat' match.matched_user.id %}" 
                       class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm">
                        Start Chat
                    </a>
                    {% endif %}
                </div>
            </div>
            {% empty %}
            <p class="text-gray-400 text-center py-4">No sent requests.</p>
            {% endfor %}
        </div>
    </div>
</div>
{% endblock %}''',

    'chat/templates/chat/chat_list.html': '''{% extends 'base.html' %}

{% block title %}Chats - Skill Swap{% endblock %}

{% block content %}
<div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-blue-400 mb-8">My Chats</h1>
    
    <div class="bg-dark-card rounded-lg shadow-xl border border-dark-border">
        <div class="divide-y divide-dark-border">
            {% for room in rooms %}
            <a href="{% url 'chat:chat_room' room.name %}" 
               class="block p-6 hover:bg-dark-bg transition">
                <div class="flex items-center justify-between">
                    <div>
                        <h3 class="text-lg font-semibold text-white">
                            {% for user in room.participants.all %}
                                {% if user != request.user %}{{ user.username }}{% endif %}
                            {% endfor %}
                        </h3>
                        <p class="text-sm text-gray-400">{{ room.updated_at|date:"M d, Y g:i A" }}</p>
                    </div>
                    <span class="text-blue-400">→</span>
                </div>
            </a>
            {% empty %}
            <div class="p-8 text-center text-gray-400">
                No chats yet. Start connecting with other users!
            </div>
            {% endfor %}
        </div>
    </div>
</div>
{% endblock %}''',

    'chat/templates/chat/chat_room.html': '''{% extends 'base.html' %}

{% block title %}Chat with {{ other_user.username }} - Skill Swap{% endblock %}

{% block content %}
<div class="max-w-4xl mx-auto">
    <div class="bg-dark-card rounded-lg shadow-xl border border-dark-border flex flex-col" style="height: 70vh;">
        <!-- Chat Header -->
        <div class="p-4 border-b border-dark-border flex justify-between items-center">
            <div>
                <h2 class="text-xl font-bold text-white">{{ other_user.username }}</h2>
                <p class="text-sm text-gray-400">Online</p>
            </div>
            <a href="{% url 'video:start_call' other_user.id %}" 
               class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-md text-sm">
                Video Call
            </a>
        </div>
        
        <!-- Messages -->
        <div id="chat-messages" class="flex-1 overflow-y-auto p-4 space-y-4">
            {% for message in messages %}
            <div class="flex {% if message.sender == request.user %}justify-end{% else %}justify-start{% endif %}">
                <div class="max-w-xs lg:max-w-md">
                    <div class="{% if message.sender == request.user %}bg-blue-600{% else %}bg-dark-bg border border-dark-border{% endif %} rounded-lg p-3">
                        <p class="text-sm text-white">{{ message.content }}</p>
                    </div>
                    <p class="text-xs text-gray-500 mt-1">{{ message.timestamp|date:"g:i A" }}</p>
                </div>
            </div>
            {% endfor %}
        </div>
        
        <!-- Message Input -->
        <div class="p-4 border-t border-dark-border">
            <div class="flex space-x-2">
                <input type="text" id="message-input" placeholder="Type your message..." 
                       class="flex-1 bg-dark-bg border border-dark-border rounded-md px-4 py-2 text-gray-100 focus:outline-none focus:border-blue-500">
                <button id="send-button" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-md">
                    Send
                </button>
            </div>
        </div>
    </div>
</div>

<script>
    const roomName = "{{ room.name }}";
    const username = "{{ request.user.username }}";
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const messagesDiv = document.getElementById('chat-messages');
        
        const messageDiv = document.createElement('div');
        messageDiv.className = 'flex ' + (data.username === username ? 'justify-end' : 'justify-start');
        
        messageDiv.innerHTML = `
            <div class="max-w-xs lg:max-w-md">
                <div class="${data.username === username ? 'bg-blue-600' : 'bg-dark-bg border border-dark-border'} rounded-lg p-3">
                    <p class="text-sm text-white">${data.message}</p>
                </div>
                <p class="text-xs text-gray-500 mt-1">Just now</p>
            </div>
        `;
        
        messagesDiv.appendChild(messageDiv);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    function sendMessage() {
        const messageInput = document.getElementById('message-input');
        const message = messageInput.value.trim();
        
        if (message) {
            chatSocket.send(JSON.stringify({
                'message': message,
                'username': username
            }));
            messageInput.value = '';
        }
    }

    document.getElementById('send-button').onclick = sendMessage;
    document.getElementById('message-input').onkeypress = function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    };

    // Scroll to bottom on load
    document.getElementById('chat-messages').scrollTop = document.getElementById('chat-messages').scrollHeight;
</script>
{% endblock %}''',

    'video/templates/video/call_list.html': '''{% extends 'base.html' %}

{% block title %}Video Calls - Skill Swap{% endblock %}

{% block content %}
<div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-blue-400 mb-8">Video Call History</h1>
    
    <div class="bg-dark-card rounded-lg shadow-xl border border-dark-border">
        <div class="divide-y divide-dark-border">
            {% for call in calls %}
            <div class="p-6">
                <div class="flex items-center justify-between">
                    <div>
                        <h3 class="text-lg font-semibold text-white">
                            {% if call.caller == request.user %}
                                Call to {{ call.receiver.username }}
                            {% else %}
                                Call from {{ call.caller.username }}
                            {% endif %}
                        </h3>
                        <p class="text-sm text-gray-400">{{ call.started_at|date:"M d, Y g:i A" }}</p>
                        <span class="inline-block mt-2 text-xs px-2 py-1 rounded
                            {% if call.status == 'active' %}bg-green-900 text-green-200
                            {% elif call.status == 'ended' %}bg-gray-700 text-gray-300
                            {% elif call.status == 'missed' %}bg-red-900 text-red-200
                            {% else %}bg-yellow-900 text-yellow-200{% endif %}">
                            {{ call.get_status_display }}
                        </span>
                    </div>
                    {% if call.status == 'active' %}
                    <a href="{% url 'video:video_room' call.room_id %}" 
                       class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-md text-sm">
                        Join Call
                    </a>
                    {% endif %}
                </div>
            </div>
            {% empty %}
            <div class="p-8 text-center text-gray-400">
                No video call history.
            </div>
            {% endfor %}
        </div>
    </div>
</div>
{% endblock %}''',

    'video/templates/video/video_room.html': '''{% extends 'base.html' %}

{% block title %}Video Call - Skill Swap{% endblock %}

{% block content %}
<div class="max-w-6xl mx-auto">
    <div class="bg-dark-card rounded-lg shadow-xl border border-dark-border p-6">
        <div class="flex justify-between items-center mb-4">
            <h2 class="text-2xl font-bold text-white">
                Video Call with 
                {% if call.caller == request.user %}
                    {{ call.receiver.username }}
                {% else %}
                    {{ call.caller.username }}
                {% endif %}
            </h2>
            <button id="end-call" class="bg-red-600 hover:bg-red-700 text-white px-6 py-2 rounded-md">
                End Call
            </button>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-dark-bg rounded-lg aspect-video flex items-center justify-center relative">
                <video id="remote-video" autoplay playsinline class="w-full h-full rounded-lg"></video>
                <p class="absolute text-gray-400">Remote Video</p>
            </div>
            <div class="bg-dark-bg rounded-lg aspect-video flex items-center justify-center relative">
                <video id="local-video" autoplay muted playsinline class="w-full h-full rounded-lg"></video>
                <p class="absolute text-gray-400">Your Video</p>
            </div>
        </div>
        
        <div class="mt-6 flex justify-center space-x-4">
            <button id="toggle-audio" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-md">
                Mute Audio
            </button>
            <button id="toggle-video" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-md">
                Stop Video
            </button>
        </div>
        
        <div class="mt-4 p-4 bg-yellow-900 border border-yellow-700 rounded-lg">
            <p class="text-yellow-200 text-sm">
                <strong>Note:</strong> For full video calling functionality, you would need to integrate a WebRTC service like 
                Agora, Twilio, or implement a custom TURN/STUN server setup.
            </p>
        </div>
    </div>
</div>

<script>
    let localStream;
    let audioEnabled = true;
    let videoEnabled = true;

    // Get user media
    async function startLocalStream() {
        try {
            localStream = await navigator.mediaDevices.getUserMedia({ 
                video: true, 
                audio: true 
            });
            document.getElementById('local-video').srcObject = localStream;
        } catch (error) {
            console.error('Error accessing media devices:', error);
            alert('Unable to access camera/microphone');
        }
    }

    // Toggle audio
    document.getElementById('toggle-audio').onclick = function() {
        audioEnabled = !audioEnabled;
        localStream.getAudioTracks()[0].enabled = audioEnabled;
        this.textContent = audioEnabled ? 'Mute Audio' : 'Unmute Audio';
        this.classList.toggle('bg-red-600');
    };

    // Toggle video
    document.getElementById('toggle-video').onclick = function() {
        videoEnabled = !videoEnabled;
        localStream.getVideoTracks()[0].enabled = videoEnabled;
        this.textContent = videoEnabled ? 'Stop Video' : 'Start Video';
        this.classList.toggle('bg-red-600');
    };

    // End call
    document.getElementById('end-call').onclick = function() {
        if (localStream) {
            localStream.getTracks().forEach(track => track.stop());
        }
        window.location.href = "{% url 'video:call_list' %}";
    };

    // Start on load
    startLocalStream();
</script>
{% endblock %}''',
}

def create_templates():
    """Create all template files"""
    print("Creating template files...")
    
    for file_path, content in TEMPLATES.items():
        full_path = BASE_DIR / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {file_path}")
    
    print("\\n✅ All templates created successfully!")

if __name__ == '__main__':
    create_templates()
