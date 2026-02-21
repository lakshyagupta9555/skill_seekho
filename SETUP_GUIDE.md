# Complete Setup Guide for Skill Swap Platform

## Quick Start

Follow these steps to set up the Skill Swap platform:

### 1. Run the build scripts

```bash
# First, create the project structure
python build_project.py

# Then, create all template files
python build_templates.py
```

### 2. Install dependencies

```bash
# Activate virtual environment
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### 3. Initialize the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a superuser

```bash
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

### 6. Access the application

- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Features

### User Management
- User registration and authentication
- Profile management with bio, photo, location
- Skill listing (can teach / want to learn)

### Dashboard
- Personalized dashboard
- Browse skills by type and search
- Find matching users based on skills
- Send/receive match requests

### Chat System
- Real-time chat using WebSockets
- One-on-one messaging
- Chat history

### Video Calling
- Video call initiation
- WebRTC-ready structure
- Call history tracking

## Project Structure

```
skill_swap/
├── skill_swap/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── users/               # User authentication & profiles
│   ├── templates/users/
│   ├── models.py
│   ├── views.py
│   └── forms.py
├── dashboard/           # Main dashboard
│   ├── templates/dashboard/
│   ├── models.py
│   └── views.py
├── chat/                # Real-time chat
│   ├── templates/chat/
│   ├── models.py
│   ├── consumers.py
│   └── routing.py
├── video/               # Video calls
│   ├── templates/video/
│   ├── models.py
│   └── views.py
├── templates/           # Base templates
├── static/              # Global static files
└── media/               # User uploads
```

## Technology Stack

- **Backend**: Django 4.x
- **Real-time**: Django Channels (WebSockets)
- **Frontend**: HTML5, Tailwind CSS 3.x, JavaScript
- **Database**: SQLite (development)
- **Video**: WebRTC-ready (needs service integration)

## Key Models

### Users App
- **Profile**: Extended user profile
- **Skill**: User skills (teach/learn)

### Dashboard App
- **SkillMatch**: Connection requests

### Chat App
- **ChatRoom**: Chat rooms between users
- **Message**: Chat messages

### Video App
- **VideoCall**: Video call sessions

## Customization

### Dark Theme
The entire UI uses a dark theme with Tailwind CSS. Colors can be customized in `base.html`:

```javascript
tailwind.config = {
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                dark: {
                    bg: '#0f172a',      // Main background
                    card: '#1e293b',    // Card background
                    border: '#334155',  // Border color
                }
            }
        }
    }
}
```

### Adding Video Call Service

For production video calling, integrate one of these services:

1. **Agora** - https://www.agora.io/
2. **Twilio** - https://www.twilio.com/
3. **Daily.co** - https://www.daily.co/
4. **Custom WebRTC** with TURN/STUN servers

## Admin Panel

Access the admin panel to:
- Manage users
- View all skills
- Monitor matches
- Check messages and calls

## Security Notes

**Important**: Before deploying to production:

1. Change `SECRET_KEY` in settings.py
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Use PostgreSQL instead of SQLite
5. Set up proper email backend
6. Configure HTTPS
7. Use Redis for Channels layer
8. Set up proper media/static file serving

## Troubleshooting

### Channels not working?
Make sure `daphne` is installed and `ASGI_APPLICATION` is set in settings.

### Static files not loading?
Run `python manage.py collectstatic`

### Database errors?
Delete `db.sqlite3` and migrations, then:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Support

For issues or questions, check:
- Django docs: https://docs.djangoproject.com/
- Channels docs: https://channels.readthedocs.io/
- Tailwind CSS: https://tailwindcss.com/docs

## License

This project is open source and available for educational purposes.
