import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Create users/profile.html
profile_html = '''{% extends 'base.html' %}

{% block title %}{{ profile_user.username }}'s Profile - SkillSwap{% endblock %}

{% block content %}
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Profile Header -->
    <div class="bg-gray-800 rounded-lg shadow-lg p-8 mb-8">
        <div class="flex items-start space-x-6">
            <div class="flex-shrink-0">
                {% if profile_user.profile_picture %}
                    <img src="{{ profile_user.profile_picture.url }}" alt="{{ profile_user.username }}" class="w-32 h-32 rounded-full object-cover border-4 border-blue-500">
                {% else %}
                    <div class="w-32 h-32 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center border-4 border-blue-500">
                        <span class="text-4xl font-bold text-white">{{ profile_user.username.0|upper }}</span>
                    </div>
                {% endif %}
            </div>
            
            <div class="flex-1">
                <div class="flex items-center justify-between">
                    <h1 class="text-3xl font-bold text-white">{{ profile_user.get_full_name|default:profile_user.username }}</h1>
                    {% if user == profile_user %}
                        <a href="{% url 'edit_profile' %}" class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200">
                            <i class="fas fa-edit mr-2"></i>Edit Profile
                        </a>
                    {% else %}
                        <a href="{% url 'create_exchange' profile_user.username %}" class="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition duration-200">
                            <i class="fas fa-handshake mr-2"></i>Request Exchange
                        </a>
                    {% endif %}
                </div>
                
                <p class="text-gray-400 mt-1">@{{ profile_user.username }}</p>
                
                {% if profile_user.location %}
                    <p class="text-gray-300 mt-2">
                        <i class="fas fa-map-marker-alt mr-2"></i>{{ profile_user.location }}
                    </p>
                {% endif %}
                
                {% if profile_user.phone %}
                    <p class="text-gray-300 mt-1">
                        <i class="fas fa-phone mr-2"></i>{{ profile_user.phone }}
                    </p>
                {% endif %}
                
                <p class="text-gray-300 mt-1">
                    <i class="fas fa-envelope mr-2"></i>{{ profile_user.email }}
                </p>
                
                {% if profile_user.bio %}
                    <p class="text-gray-300 mt-4">{{ profile_user.bio }}</p>
                {% endif %}
                
                <p class="text-gray-400 mt-4 text-sm">
                    <i class="fas fa-calendar-alt mr-2"></i>Joined {{ profile_user.date_joined|date:"F Y" }}
                </p>
            </div>
        </div>
    </div>

    <!-- Skills Section -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Teaching Skills -->
        <div class="bg-gray-800 rounded-lg shadow-lg p-6">
            <h2 class="text-2xl font-bold text-white mb-4">
                <i class="fas fa-chalkboard-teacher text-green-500 mr-2"></i>Can Teach
            </h2>
            
            {% if teaching_skills %}
                <div class="space-y-4">
                    {% for skill in teaching_skills %}
                        <div class="bg-gray-700 rounded-lg p-4">
                            <div class="flex items-center justify-between mb-2">
                                <h3 class="text-lg font-semibold text-white">{{ skill.skill_name }}</h3>
                                <span class="px-3 py-1 bg-green-600 text-white text-sm rounded-full">{{ skill.get_proficiency_display }}</span>
                            </div>
                            {% if skill.description %}
                                <p class="text-gray-300">{{ skill.description }}</p>
                            {% endif %}
                        </div>
                    {% endfor %}
                </div>
            {% else %}
                <p class="text-gray-400">No teaching skills listed yet.</p>
            {% endif %}
        </div>

        <!-- Learning Interests -->
        <div class="bg-gray-800 rounded-lg shadow-lg p-6">
            <h2 class="text-2xl font-bold text-white mb-4">
                <i class="fas fa-book-reader text-blue-500 mr-2"></i>Wants to Learn
            </h2>
            
            {% if learning_interests %}
                <div class="space-y-4">
                    {% for interest in learning_interests %}
                        <div class="bg-gray-700 rounded-lg p-4">
                            <h3 class="text-lg font-semibold text-white mb-2">{{ interest.skill_name }}</h3>
                            {% if interest.description %}
                                <p class="text-gray-300">{{ interest.description }}</p>
                            {% endif %}
                        </div>
                    {% endfor %}
                </div>
            {% else %}
                <p class="text-gray-400">No learning interests listed yet.</p>
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}
'''

# Ensure directory exists
users_template_dir = os.path.join(TEMPLATES_DIR, 'users')
os.makedirs(users_template_dir, exist_ok=True)

# Write profile.html
profile_path = os.path.join(users_template_dir, 'profile.html')
with open(profile_path, 'w', encoding='utf-8') as f:
    f.write(profile_html)

print(f"✓ Created: {profile_path}")

# Create users/add_skill.html if it's empty or missing
add_skill_html = '''{% extends 'base.html' %}

{% block title %}Add Teaching Skill - SkillSwap{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8">
        <h1 class="text-3xl font-bold text-white mb-8">Add a Teaching Skill</h1>
        
        <form method="post" class="space-y-6">
            {% csrf_token %}
            
            <div>
                <label for="id_skill_name" class="block text-sm font-medium text-gray-300 mb-2">Skill Name *</label>
                {{ form.skill_name }}
            </div>
            
            <div>
                <label for="id_proficiency" class="block text-sm font-medium text-gray-300 mb-2">Proficiency Level *</label>
                {{ form.proficiency }}
            </div>
            
            <div>
                <label for="id_description" class="block text-sm font-medium text-gray-300 mb-2">Description</label>
                {{ form.description }}
            </div>
            
            <div class="flex justify-end space-x-4">
                <a href="{% url 'dashboard' %}" class="px-6 py-2 bg-gray-700 text-white rounded-lg hover:bg-gray-600 transition duration-200">
                    Cancel
                </a>
                <button type="submit" class="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition duration-200">
                    <i class="fas fa-plus mr-2"></i>Add Skill
                </button>
            </div>
        </form>
    </div>
</div>
{% endblock %}
'''

add_skill_path = os.path.join(users_template_dir, 'add_skill.html')
with open(add_skill_path, 'w', encoding='utf-8') as f:
    f.write(add_skill_html)

print(f"✓ Created: {add_skill_path}")

# Create users/add_interest.html
add_interest_html = '''{% extends 'base.html' %}

{% block title %}Add Learning Interest - SkillSwap{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8">
        <h1 class="text-3xl font-bold text-white mb-8">Add a Learning Interest</h1>
        
        <form method="post" class="space-y-6">
            {% csrf_token %}
            
            <div>
                <label for="id_skill_name" class="block text-sm font-medium text-gray-300 mb-2">Skill Name *</label>
                {{ form.skill_name }}
            </div>
            
            <div>
                <label for="id_description" class="block text-sm font-medium text-gray-300 mb-2">Why do you want to learn this?</label>
                {{ form.description }}
            </div>
            
            <div class="flex justify-end space-x-4">
                <a href="{% url 'dashboard' %}" class="px-6 py-2 bg-gray-700 text-white rounded-lg hover:bg-gray-600 transition duration-200">
                    Cancel
                </a>
                <button type="submit" class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200">
                    <i class="fas fa-plus mr-2"></i>Add Interest
                </button>
            </div>
        </form>
    </div>
</div>
{% endblock %}
'''

add_interest_path = os.path.join(users_template_dir, 'add_interest.html')
with open(add_interest_path, 'w', encoding='utf-8') as f:
    f.write(add_interest_html)

print(f"✓ Created: {add_interest_path}")

# Create users/edit_profile.html
edit_profile_html = '''{% extends 'base.html' %}

{% block title %}Edit Profile - SkillSwap{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8">
        <h1 class="text-3xl font-bold text-white mb-8">Edit Your Profile</h1>
        
        <form method="post" enctype="multipart/form-data" class="space-y-6">
            {% csrf_token %}
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                    <label for="id_first_name" class="block text-sm font-medium text-gray-300 mb-2">First Name</label>
                    {{ form.first_name }}
                </div>
                <div>
                    <label for="id_last_name" class="block text-sm font-medium text-gray-300 mb-2">Last Name</label>
                    {{ form.last_name }}
                </div>
            </div>
            
            <div>
                <label for="id_email" class="block text-sm font-medium text-gray-300 mb-2">Email</label>
                {{ form.email }}
            </div>
            
            <div>
                <label for="id_phone" class="block text-sm font-medium text-gray-300 mb-2">Phone</label>
                {{ form.phone }}
            </div>
            
            <div>
                <label for="id_location" class="block text-sm font-medium text-gray-300 mb-2">Location</label>
                {{ form.location }}
            </div>
            
            <div>
                <label for="id_bio" class="block text-sm font-medium text-gray-300 mb-2">Bio</label>
                {{ form.bio }}
            </div>
            
            <div>
                <label for="id_profile_picture" class="block text-sm font-medium text-gray-300 mb-2">Profile Picture</label>
                {{ form.profile_picture }}
            </div>
            
            <div class="flex justify-end space-x-4">
                <a href="{% url 'profile' user.username %}" class="px-6 py-2 bg-gray-700 text-white rounded-lg hover:bg-gray-600 transition duration-200">
                    Cancel
                </a>
                <button type="submit" class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200">
                    <i class="fas fa-save mr-2"></i>Save Changes
                </button>
            </div>
        </form>
    </div>
</div>
{% endblock %}
'''

edit_profile_path = os.path.join(users_template_dir, 'edit_profile.html')
with open(edit_profile_path, 'w', encoding='utf-8') as f:
    f.write(edit_profile_html)

print(f"✓ Created: {edit_profile_path}")

# Create skills/exchange_list.html
skills_template_dir = os.path.join(TEMPLATES_DIR, 'skills')
os.makedirs(skills_template_dir, exist_ok=True)

exchange_list_html = '''{% extends 'base.html' %}

{% block title %}Skill Exchanges - SkillSwap{% endblock %}

{% block content %}
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <h1 class="text-3xl font-bold text-white mb-8">My Skill Exchanges</h1>
    
    <div class="bg-gray-800 rounded-lg shadow-lg p-6">
        {% if exchanges %}
            <div class="space-y-4">
                {% for exchange in exchanges %}
                    <div class="bg-gray-700 rounded-lg p-6 hover:bg-gray-600 transition duration-200">
                        <div class="flex items-center justify-between">
                            <div class="flex-1">
                                <h3 class="text-xl font-semibold text-white">
                                    {% if exchange.requester == user %}
                                        Exchange with {{ exchange.responder.username }}
                                    {% else %}
                                        Exchange with {{ exchange.requester.username }}
                                    {% endif %}
                                </h3>
                                <p class="text-gray-300 mt-2">
                                    <span class="text-green-400">Teaching:</span> {{ exchange.offered_skill }}
                                    <span class="mx-2">↔</span>
                                    <span class="text-blue-400">Learning:</span> {{ exchange.requested_skill }}
                                </p>
                                <p class="text-gray-400 text-sm mt-2">Status: {{ exchange.get_status_display }}</p>
                            </div>
                            <a href="{% url 'exchange_detail' exchange.id %}" class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200">
                                View Details
                            </a>
                        </div>
                    </div>
                {% endfor %}
            </div>
        {% else %}
            <p class="text-gray-400 text-center py-8">No exchanges yet. Start searching for users!</p>
        {% endif %}
    </div>
</div>
{% endblock %}
'''

exchange_list_path = os.path.join(skills_template_dir, 'exchange_list.html')
with open(exchange_list_path, 'w', encoding='utf-8') as f:
    f.write(exchange_list_html)

print(f"✓ Created: {exchange_list_path}")

# Create skills/create_exchange.html
create_exchange_html = '''{% extends 'base.html' %}

{% block title %}Create Exchange - SkillSwap{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8">
        <h1 class="text-3xl font-bold text-white mb-8">Request Skill Exchange</h1>
        
        <div class="bg-gray-700 rounded-lg p-4 mb-6">
            <p class="text-gray-300">Requesting exchange with: <span class="font-semibold text-white">{{ responder.username }}</span></p>
        </div>
        
        <form method="post" class="space-y-6">
            {% csrf_token %}
            
            <div>
                <label for="id_offered_skill" class="block text-sm font-medium text-gray-300 mb-2">What will you teach? *</label>
                {{ form.offered_skill }}
            </div>
            
            <div>
                <label for="id_requested_skill" class="block text-sm font-medium text-gray-300 mb-2">What do you want to learn? *</label>
                {{ form.requested_skill }}
            </div>
            
            <div>
                <label for="id_message" class="block text-sm font-medium text-gray-300 mb-2">Message</label>
                {{ form.message }}
            </div>
            
            <div class="flex justify-end space-x-4">
                <a href="{% url 'profile' responder.username %}" class="px-6 py-2 bg-gray-700 text-white rounded-lg hover:bg-gray-600 transition duration-200">
                    Cancel
                </a>
                <button type="submit" class="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition duration-200">
                    <i class="fas fa-handshake mr-2"></i>Send Request
                </button>
            </div>
        </form>
    </div>
</div>
{% endblock %}
'''

create_exchange_path = os.path.join(skills_template_dir, 'create_exchange.html')
with open(create_exchange_path, 'w', encoding='utf-8') as f:
    f.write(create_exchange_html)

print(f"✓ Created: {create_exchange_path}")

# Create chat/chat_list.html
chat_template_dir = os.path.join(TEMPLATES_DIR, 'chat')
os.makedirs(chat_template_dir, exist_ok=True)

chat_list_html = '''{% extends 'base.html' %}

{% block title %}Chats - SkillSwap{% endblock %}

{% block content %}
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <h1 class="text-3xl font-bold text-white mb-8">My Chats</h1>
    
    <div class="bg-gray-800 rounded-lg shadow-lg p-6">
        {% if chat_rooms %}
            <div class="space-y-4">
                {% for room in chat_rooms %}
                    <a href="{% url 'chat_room' room.id %}" class="block bg-gray-700 rounded-lg p-6 hover:bg-gray-600 transition duration-200">
                        <div class="flex items-center justify-between">
                            <div>
                                <h3 class="text-xl font-semibold text-white">
                                    {% if room.exchange.requester == user %}
                                        Chat with {{ room.exchange.responder.username }}
                                    {% else %}
                                        Chat with {{ room.exchange.requester.username }}
                                    {% endif %}
                                </h3>
                                <p class="text-gray-400 mt-1">{{ room.exchange.offered_skill }} ↔ {{ room.exchange.requested_skill }}</p>
                            </div>
                            <i class="fas fa-chevron-right text-gray-400"></i>
                        </div>
                    </a>
                {% endfor %}
            </div>
        {% else %}
            <p class="text-gray-400 text-center py-8">No active chats yet.</p>
        {% endif %}
    </div>
</div>
{% endblock %}
'''

chat_list_path = os.path.join(chat_template_dir, 'chat_list.html')
with open(chat_list_path, 'w', encoding='utf-8') as f:
    f.write(chat_list_html)

print(f"✓ Created: {chat_list_path}")

print("\n✅ All templates created successfully!")
