# Create Django Skill Swap Platform
import os

# Define directory structure
directories = [
    'skill_swap',
    'users\\templates\\users',
    'users\\static\\users\\css',
    'users\\static\\users\\js',
    'dashboard\\templates\\dashboard',
    'dashboard\\static\\dashboard\\css',
    'dashboard\\static\\dashboard\\js',
    'chat\\templates\\chat',
    'chat\\static\\chat\\css',
    'chat\\static\\chat\\js',
    'video\\templates\\video',
    'video\\static\\video\\css',
    'video\\static\\video\\js',
    'static\\css',
    'static\\js',
    'media\\profile_pics',
    'media\\skill_images',
    'templates',
]

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"Created: {directory}")

print("\nDirectory structure created successfully!")
