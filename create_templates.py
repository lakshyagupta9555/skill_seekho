"""
Script to create all missing or empty template files for SkillSwap
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Template content dictionary
TEMPLATES = {
    'users/profile.html': '''{% extends 'base.html' %}

{% block title %}{{ profile_user.username }}'s Profile{% endblock %}

{% block content %}
<div class="max-w-4xl mx-auto">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8 mb-6 border border-gray-700">
        <div class="flex items-start space-x-6">
            {% if profile_user.profile_picture %}
            <img src="{{ profile_user.profile_picture.url }}" alt="{{ profile_user.username }}" class="w-32 h-32 rounded-full">
            {% else %}
            <div class="w-32 h-32 rounded-full bg-gradient-to-r from-blue-600 to-purple-600 text-white flex items-center justify-center text-4xl font-bold">
                {{ profile_user.username.0|upper }}
            </div>
            {% endif %}
            
            <div class="flex-1">
                <h1 class="text-3xl font-bold text-gray-100">{{ profile_user.get_full_name|default:profile_user.username }}</h1>
                <p class="text-gray-400 text-lg">@{{ profile_user.username }}</p>
                
                {% if profile_user.bio %}
                <p class="mt-4 text-gray-300">{{ profile_user.bio }}</p>
                {% endif %}
                
                {% if user == profile_user %}
                <div class="mt-4">
                    <a href="{% url 'edit_profile' %}" class="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700">Edit Profile</a>
                </div>
                {% else %}
                <div class="mt-4 space-x-3">
                    <a href="{% url 'create_exchange' profile_user.username %}" class="bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700">Start Exchange</a>
                </div>
                {% endif %}
            </div>
        </div>
    </div>
    
    <div class="grid md:grid-cols-2 gap-6">
        <div class="bg-gray-800 rounded-lg shadow-lg p-6 border border-gray-700">
            <h2 class="text-2xl font-bold text-gray-100 mb-4">Can Teach</h2>
            {% if teaching_skills %}
            <div class="space-y-3">
                {% for skill in teaching_skills %}
                <div class="border border-gray-700 rounded-lg p-4">
                    <h3 class="font-semibold text-gray-100">{{ skill.skill_name }}</h3>
                    <p class="text-sm text-gray-400">Level: {{ skill.get_skill_level_display }}</p>
                </div>
                {% endfor %}
            </div>
            {% else %}
            <p class="text-gray-400">No skills listed.</p>
            {% endif %}
        </div>
        
        <div class="bg-gray-800 rounded-lg shadow-lg p-6 border border-gray-700">
            <h2 class="text-2xl font-bold text-gray-100 mb-4">Wants to Learn</h2>
            {% if learning_interests %}
            <div class="space-y-3">
                {% for interest in learning_interests %}
                <div class="border border-gray-700 rounded-lg p-4">
                    <h3 class="font-semibold text-gray-100">{{ interest.skill_name }}</h3>
                </div>
                {% endfor %}
            </div>
            {% else %}
            <p class="text-gray-400">No interests listed.</p>
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}
''',
    
    'users/edit_profile.html': '''{% extends 'base.html' %}

{% block title %}Edit Profile{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8 border border-gray-700">
        <h2 class="text-2xl font-bold text-gray-100 mb-6">Edit Profile</h2>
        
        <form method="POST" enctype="multipart/form-data" class="space-y-6">
            {% csrf_token %}
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">First Name</label>
                <input type="text" name="first_name" value="{{ form.first_name.value|default:'' }}" 
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500">
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Last Name</label>
                <input type="text" name="last_name" value="{{ form.last_name.value|default:'' }}" 
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500">
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Email</label>
                <input type="email" name="email" value="{{ form.email.value|default:'' }}" 
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500">
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Bio</label>
                <textarea name="bio" rows="4" 
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500">{{ form.bio.value|default:'' }}</textarea>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Phone</label>
                <input type="text" name="phone" value="{{ form.phone.value|default:'' }}" 
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500">
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Location</label>
                <input type="text" name="location" value="{{ form.location.value|default:'' }}" 
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500">
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Profile Picture</label>
                <input type="file" name="profile_picture" accept="image/*"
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg">
            </div>
            
            <div class="flex space-x-4">
                <button type="submit" class="flex-1 bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700">Save</button>
                <a href="{% url 'dashboard' %}" class="flex-1 bg-gray-700 text-gray-100 px-6 py-3 rounded-lg hover:bg-gray-600 text-center">Cancel</a>
            </div>
        </form>
    </div>
</div>
{% endblock %}
''',
    
    'users/add_skill.html': '''{% extends 'base.html' %}

{% block title %}Add Skill{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8 border border-gray-700">
        <h2 class="text-2xl font-bold text-gray-100 mb-6">Add a Skill</h2>
        
        <form method="POST" class="space-y-6">
            {% csrf_token %}
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Skill Name *</label>
                <input type="text" name="skill_name" required
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500"
                    placeholder="e.g., Python Programming">
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Level *</label>
                <select name="skill_level" required class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg">
                    <option value="">Select level</option>
                    <option value="beginner">Beginner</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="advanced">Advanced</option>
                    <option value="expert">Expert</option>
                </select>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Category *</label>
                <select name="is_tech" required class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg">
                    <option value="">Select category</option>
                    <option value="True">Tech</option>
                    <option value="False">Non-Tech</option>
                </select>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Description</label>
                <textarea name="description" rows="4"
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg"></textarea>
            </div>
            
            <div class="flex space-x-4">
                <button type="submit" class="flex-1 bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700">Add Skill</button>
                <a href="{% url 'dashboard' %}" class="flex-1 bg-gray-700 text-gray-100 px-6 py-3 rounded-lg hover:bg-gray-600 text-center">Cancel</a>
            </div>
        </form>
    </div>
</div>
{% endblock %}
''',
    
    'users/add_interest.html': '''{% extends 'base.html' %}

{% block title %}Add Interest{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8 border border-gray-700">
        <h2 class="text-2xl font-bold text-gray-100 mb-6">Add Learning Interest</h2>
        
        <form method="POST" class="space-y-6">
            {% csrf_token %}
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Skill Name *</label>
                <input type="text" name="skill_name" required
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500"
                    placeholder="What do you want to learn?">
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Category *</label>
                <select name="is_tech" required class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg">
                    <option value="">Select category</option>
                    <option value="True">Tech</option>
                    <option value="False">Non-Tech</option>
                </select>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Description</label>
                <textarea name="description" rows="4"
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg"></textarea>
            </div>
            
            <div class="flex space-x-4">
                <button type="submit" class="flex-1 bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700">Add Interest</button>
                <a href="{% url 'dashboard' %}" class="flex-1 bg-gray-700 text-gray-100 px-6 py-3 rounded-lg hover:bg-gray-600 text-center">Cancel</a>
            </div>
        </form>
    </div>
</div>
{% endblock %}
''',
    
    'users/search.html': '''{% extends 'base.html' %}

{% block title %}Search Users{% endblock %}

{% block content %}
<div>
    <h1 class="text-3xl font-bold text-gray-100 mb-6">Find Skills</h1>
    
    <div class="bg-gray-800 rounded-lg shadow-lg p-6 mb-6 border border-gray-700">
        <form method="GET" class="flex space-x-4">
            <input type="text" name="q" value="{{ query }}" placeholder="Search skills..."
                class="flex-1 px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500">
            <button type="submit" class="bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700">Search</button>
        </form>
    </div>
    
    {% if users %}
    <div class="grid md:grid-cols-2 gap-6">
        {% for user_obj in users %}
        <div class="bg-gray-800 rounded-lg shadow-lg p-6 border border-gray-700">
            <h3 class="text-xl font-bold text-gray-100">{{ user_obj.get_full_name|default:user_obj.username }}</h3>
            <p class="text-gray-400">@{{ user_obj.username }}</p>
            <a href="{% url 'profile' user_obj.username %}" class="mt-4 inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">View Profile</a>
        </div>
        {% endfor %}
    </div>
    {% else %}
    <p class="text-gray-400">No users found.</p>
    {% endif %}
</div>
{% endblock %}
''',

    'skills/exchange_list.html': '''{% extends 'base.html' %}

{% block title %}Skill Exchanges{% endblock %}

{% block content %}
<div>
    <h1 class="text-3xl font-bold text-gray-100 mb-6">My Exchanges</h1>
    
    {% if exchanges %}
    <div class="space-y-4">
        {% for exchange in exchanges %}
        <div class="bg-gray-800 rounded-lg shadow-lg p-6 border border-gray-700">
            <h3 class="text-xl font-bold text-gray-100">Exchange with {{ exchange.responder.username }}</h3>
            <p class="text-gray-400">Status: {{ exchange.get_status_display }}</p>
            <a href="{% url 'exchange_detail' exchange.id %}" class="mt-2 inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">View</a>
        </div>
        {% endfor %}
    </div>
    {% else %}
    <p class="text-gray-400">No exchanges yet.</p>
    {% endif %}
</div>
{% endblock %}
''',

    'skills/exchange_detail.html': '''{% extends 'base.html' %}

{% block title %}Exchange Details{% endblock %}

{% block content %}
<div class="max-w-4xl mx-auto">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8 border border-gray-700">
        <h1 class="text-3xl font-bold text-gray-100 mb-4">Skill Exchange</h1>
        <p class="text-gray-300 mb-6">Status: {{ exchange.get_status_display }}</p>
        
        <div class="grid md:grid-cols-2 gap-6">
            <div>
                <h3 class="text-xl font-bold text-gray-100 mb-2">Requester</h3>
                <p class="text-gray-300">{{ exchange.requester.get_full_name|default:exchange.requester.username }}</p>
            </div>
            <div>
                <h3 class="text-xl font-bold text-gray-100 mb-2">Responder</h3>
                <p class="text-gray-300">{{ exchange.responder.get_full_name|default:exchange.responder.username }}</p>
            </div>
        </div>
        
        {% if exchange.chat_room %}
        <div class="mt-6">
            <a href="{% url 'chat_room' exchange.chat_room.id %}" class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700">Go to Chat</a>
        </div>
        {% endif %}
    </div>
</div>
{% endblock %}
''',

    'skills/create_exchange.html': '''{% extends 'base.html' %}

{% block title %}Create Exchange{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8 border border-gray-700">
        <h2 class="text-2xl font-bold text-gray-100 mb-6">Start Exchange</h2>
        
        <form method="POST" class="space-y-6">
            {% csrf_token %}
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Skill to Teach</label>
                <select name="skill_offered" required class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg">
                    <option value="">Select your skill</option>
                    {% for skill in user_skills %}
                    <option value="{{ skill.id }}">{{ skill.skill_name }}</option>
                    {% endfor %}
                </select>
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Skill to Learn</label>
                <select name="skill_requested" required class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg">
                    <option value="">Select skill to learn</option>
                    {% for skill in partner_skills %}
                    <option value="{{ skill.id }}">{{ skill.skill_name }}</option>
                    {% endfor %}
                </select>
            </div>
            
            <div class="flex space-x-4">
                <button type="submit" class="flex-1 bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700">Create Exchange</button>
                <a href="{% url 'dashboard' %}" class="flex-1 bg-gray-700 text-gray-100 px-6 py-3 rounded-lg hover:bg-gray-600 text-center">Cancel</a>
            </div>
        </form>
    </div>
</div>
{% endblock %}
''',

    'chat/chat_list.html': '''{% extends 'base.html' %}

{% block title %}Chats{% endblock %}

{% block content %}
<div>
    <h1 class="text-3xl font-bold text-gray-100 mb-6">My Chats</h1>
    
    {% if chat_rooms %}
    <div class="space-y-4">
        {% for room in chat_rooms %}
        <div class="bg-gray-800 rounded-lg shadow-lg p-6 border border-gray-700">
            <h3 class="text-xl font-bold text-gray-100">Chat Room</h3>
            <a href="{% url 'chat_room' room.id %}" class="mt-2 inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Open Chat</a>
        </div>
        {% endfor %}
    </div>
    {% else %}
    <p class="text-gray-400">No active chats.</p>
    {% endif %}
</div>
{% endblock %}
''',

    'chat/chat_room.html': '''{% extends 'base.html' %}

{% block title %}Chat Room{% endblock %}

{% block content %}
<div class="max-w-4xl mx-auto">
    <div class="bg-gray-800 rounded-lg shadow-lg border border-gray-700" style="height: 600px; display: flex; flex-direction: column;">
        <div class="p-4 border-b border-gray-700">
            <h2 class="text-xl font-bold text-gray-100">Chat</h2>
        </div>
        
        <div id="chat-messages" class="flex-1 overflow-y-auto p-4 space-y-3">
            <!-- Messages will appear here -->
        </div>
        
        <div class="p-4 border-t border-gray-700">
            <form id="chat-form" class="flex space-x-3">
                <input type="text" id="chat-message-input" placeholder="Type a message..."
                    class="flex-1 px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg focus:ring-2 focus:ring-blue-500">
                <button type="submit" class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700">Send</button>
            </form>
        </div>
    </div>
</div>

<script>
    const roomId = {{ room.id }};
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + roomId + '/'
    );
    
    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const messagesDiv = document.getElementById('chat-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = 'bg-gray-700 rounded p-3';
        messageDiv.innerHTML = '<strong class="text-blue-400">' + data.username + ':</strong> <span class="text-gray-200">' + data.message + '</span>';
        messagesDiv.appendChild(messageDiv);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    };
    
    document.getElementById('chat-form').onsubmit = function(e) {
        e.preventDefault();
        const messageInput = document.getElementById('chat-message-input');
        chatSocket.send(JSON.stringify({
            'message': messageInput.value
        }));
        messageInput.value = '';
    };
</script>
{% endblock %}
''',

    'meetings/meeting_list.html': '''{% extends 'base.html' %}

{% block title %}Meetings{% endblock %}

{% block content %}
<div>
    <h1 class="text-3xl font-bold text-gray-100 mb-6">My Meetings</h1>
    
    {% if meetings %}
    <div class="space-y-4">
        {% for meeting in meetings %}
        <div class="bg-gray-800 rounded-lg shadow-lg p-6 border border-gray-700">
            <h3 class="text-xl font-bold text-gray-100">Meeting at {{ meeting.scheduled_time|date:"M d, Y H:i" }}</h3>
            <p class="text-gray-400">Status: {{ meeting.get_status_display }}</p>
            <a href="{% url 'meeting_detail' meeting.id %}" class="mt-2 inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">View</a>
        </div>
        {% endfor %}
    </div>
    {% else %}
    <p class="text-gray-400">No meetings scheduled.</p>
    {% endif %}
</div>
{% endblock %}
''',

    'meetings/meeting_detail.html': '''{% extends 'base.html' %}

{% block title %}Meeting Details{% endblock %}

{% block content %}
<div class="max-w-4xl mx-auto">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8 border border-gray-700">
        <h1 class="text-3xl font-bold text-gray-100 mb-4">Video Meeting</h1>
        <p class="text-gray-300 mb-2">Time: {{ meeting.scheduled_time|date:"M d, Y H:i" }}</p>
        <p class="text-gray-300 mb-6">Status: {{ meeting.get_status_display }}</p>
        
        {% if meeting.meeting_link %}
        <a href="{{ meeting.meeting_link }}" target="_blank" class="bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700">Join Meeting</a>
        {% else %}
        <p class="text-gray-400">No meeting link available yet.</p>
        {% endif %}
    </div>
</div>
{% endblock %}
''',

    'meetings/create_meeting.html': '''{% extends 'base.html' %}

{% block title %}Schedule Meeting{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto">
    <div class="bg-gray-800 rounded-lg shadow-lg p-8 border border-gray-700">
        <h2 class="text-2xl font-bold text-gray-100 mb-6">Schedule a Meeting</h2>
        
        <form method="POST" class="space-y-6">
            {% csrf_token %}
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Date & Time</label>
                <input type="datetime-local" name="scheduled_time" required
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg">
            </div>
            
            <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Meeting Link (optional)</label>
                <input type="url" name="meeting_link"
                    class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-gray-100 rounded-lg"
                    placeholder="https://zoom.us/j/...">
            </div>
            
            <div class="flex space-x-4">
                <button type="submit" class="flex-1 bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700">Schedule</button>
                <a href="{% url 'meeting_list' %}" class="flex-1 bg-gray-700 text-gray-100 px-6 py-3 rounded-lg hover:bg-gray-600 text-center">Cancel</a>
            </div>
        </form>
    </div>
</div>
{% endblock %}
''',
}

def create_templates():
    """Create all template files"""
    print("Creating template files...")
    
    for template_path, content in TEMPLATES.items():
        full_path = os.path.join(TEMPLATES_DIR, template_path)
        dir_path = os.path.dirname(full_path)
        
        # Create directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)
        
        # Write template file
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created: {template_path}")
    
    print("\n✅ All templates created successfully!")

if __name__ == '__main__':
    create_templates()
