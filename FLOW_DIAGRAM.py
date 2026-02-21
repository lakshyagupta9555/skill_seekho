"""
Create a visual diagram of the application flow
"""

def print_diagram():
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                      SKILL SWAP PLATFORM - FLOW DIAGRAM                      ║
╚══════════════════════════════════════════════════════════════════════════════╝


┌─────────────────────────────────────────────────────────────────────────────┐
│                            USER JOURNEY FLOW                                 │
└─────────────────────────────────────────────────────────────────────────────┘

    START
      │
      ▼
 ┌─────────┐
 │  Visit  │
 │   Site  │
 └────┬────┘
      │
      ├──────────────────┬─────────────────┐
      ▼                  ▼                 ▼
 ┌─────────┐      ┌──────────┐      ┌──────────┐
 │  Login  │      │ Register │      │  Browse  │
 └────┬────┘      └────┬─────┘      │  (Guest) │
      │                │             └──────────┘
      │                │
      ▼                ▼
 ┌──────────────────────────────────┐
 │         DASHBOARD HOME            │
 │  • View stats                    │
 │  • See potential matches         │
 │  • Quick actions                 │
 └─────────────┬────────────────────┘
               │
      ┌────────┼────────┬────────────┬────────────┐
      ▼        ▼        ▼            ▼            ▼
 ┌─────────┐ ┌────┐ ┌────────┐ ┌────────┐ ┌────────┐
 │ Profile │ │Browse│ │Matches │ │  Chat  │ │ Video │
 └────┬────┘ └──┬─┘ └───┬────┘ └───┬────┘ └───┬───┘
      │         │       │           │           │
      ▼         │       │           │           │
 ┌─────────┐   │       │           │           │
 │Add Skill│   │       │           │           │
 └────┬────┘   │       │           │           │
      │         │       │           │           │
      └─────────┴───────┴───────────┴───────────┘
                        │
                        ▼
                 ┌────────────┐
                 │   SUCCESS  │
                 │ Skill Swap │
                 └────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│                          APPLICATION ARCHITECTURE                            │
└─────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│                              FRONTEND LAYER                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
│  │   HTML   │  │Tailwind  │  │JavaScript│  │WebSocket │                  │
│  │Templates │  │   CSS    │  │   DOM    │  │  Client  │                  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘                  │
└────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                            DJANGO MIDDLEWARE                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
│  │   Auth   │  │   CSRF   │  │ Session  │  │ Messages │                  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘                  │
└────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                              URL ROUTING                                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
│  │  users/  │  │dashboard/│  │  chat/   │  │  video/  │                  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘                  │
└────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                              VIEWS LAYER                                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
│  │  User    │  │Dashboard │  │   Chat   │  │  Video   │                  │
│  │  Views   │  │  Views   │  │  Views   │  │  Views   │                  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘                  │
└────────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
┌──────────────────────────────────┐  ┌──────────────────────────────────┐
│        MODELS LAYER               │  │     CHANNELS LAYER               │
│  ┌──────────┐  ┌──────────┐      │  │  ┌──────────┐  ┌──────────┐    │
│  │  Profile │  │  Skill   │      │  │  │Consumer  │  │WebSocket │    │
│  │  Match   │  │ ChatRoom │      │  │  │ Routing  │  │  Events  │    │
│  │ Message  │  │VideoCall │      │  │  └──────────┘  └──────────┘    │
│  └──────────┘  └──────────┘      │  │                                  │
└──────────────────────────────────┘  └──────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                            DATABASE LAYER                                   │
│                              SQLite / PostgreSQL                            │
└────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│                            DATA FLOW DIAGRAM                                 │
└─────────────────────────────────────────────────────────────────────────────┘

USER REGISTRATION FLOW
──────────────────────
Browser → Register Form → UserRegisterForm → User Model → Profile Signal 
       → Create Profile → Redirect to Dashboard


SKILL MATCHING FLOW
───────────────────
User adds skill → Check can_teach/want_to_learn → Find complementary skills
       → Create potential matches → Display on dashboard


CHAT FLOW (WebSocket)
─────────────────────
User sends message → WebSocket → ChatConsumer → Save to DB
       → Broadcast to room → Display to recipient


VIDEO CALL FLOW
───────────────
Initiate call → Create VideoCall record → Generate room_id
       → Navigate to video room → WebRTC connection → Start streaming


┌─────────────────────────────────────────────────────────────────────────────┐
│                         DATABASE RELATIONSHIPS                               │
└─────────────────────────────────────────────────────────────────────────────┘

User (Django Auth)
  │
  ├──1:1──> Profile
  │
  ├──1:N──> Skill (can have many)
  │           │
  │           └──> SkillMatch (references)
  │
  ├──M:N──> ChatRoom (participants)
  │           │
  │           └──1:N──> Message
  │
  └──1:N──> VideoCall (caller/receiver)


┌─────────────────────────────────────────────────────────────────────────────┐
│                         FEATURE BREAKDOWN                                    │
└─────────────────────────────────────────────────────────────────────────────┘

USERS APP
─────────
  Registration
      │
      ├─> Email validation
      ├─> Password strength
      ├─> Auto-create profile
      └─> Auto-login

  Profile
      │
      ├─> Upload photo (auto-resize)
      ├─> Edit bio
      ├─> Update location
      └─> Manage skills

  Skills
      │
      ├─> Add unlimited skills
      ├─> Set skill type
      ├─> Set level
      ├─> Mark teach/learn
      └─> Delete skills


DASHBOARD APP
─────────────
  Home
      │
      ├─> Display stats
      ├─> Show potential matches
      ├─> Quick navigation
      └─> Recent activity

  Browse
      │
      ├─> Filter by type
      ├─> Search by name
      ├─> View all skills
      └─> Send requests

  Matches
      │
      ├─> View received requests
      ├─> View sent requests
      ├─> Accept/reject
      └─> Start chat


CHAT APP
────────
  Chat List
      │
      ├─> Show all conversations
      ├─> Last message preview
      ├─> Unread count
      └─> Sort by recent

  Chat Room
      │
      ├─> Real-time messaging
      ├─> Message history
      ├─> Online status
      ├─> Video call button
      └─> Typing indicators


VIDEO APP
─────────
  Call List
      │
      ├─> Call history
      ├─> Call status
      ├─> Duration
      └─> Rejoin active calls

  Video Room
      │
      ├─> Local video
      ├─> Remote video
      ├─> Mute/unmute
      ├─> Video on/off
      └─> End call


┌─────────────────────────────────────────────────────────────────────────────┐
│                           TECHNOLOGY STACK                                   │
└─────────────────────────────────────────────────────────────────────────────┘

Backend
───────
  Django 4.2+
      │
      ├─> ORM (Database)
      ├─> Admin panel
      ├─> Authentication
      ├─> Forms
      └─> Templates

  Django Channels
      │
      ├─> WebSocket support
      ├─> ASGI server
      ├─> Consumers
      └─> Routing

Frontend
────────
  HTML5
      │
      └─> Semantic markup

  Tailwind CSS
      │
      ├─> Utility classes
      ├─> Dark theme
      ├─> Responsive
      └─> Custom config

  JavaScript
      │
      ├─> WebSocket client
      ├─> WebRTC
      ├─> DOM manipulation
      └─> Form handling

Database
────────
  Development: SQLite
  Production: PostgreSQL

Storage
───────
  Profile pictures
  Skill images
  Static files


┌─────────────────────────────────────────────────────────────────────────────┐
│                        DEPLOYMENT CHECKLIST                                  │
└─────────────────────────────────────────────────────────────────────────────┘

□ Set environment variables
□ Change SECRET_KEY
□ DEBUG = False
□ Configure ALLOWED_HOSTS
□ Setup PostgreSQL
□ Configure Redis for Channels
□ Setup email service
□ Configure HTTPS
□ Setup Nginx/Apache
□ Configure static files CDN
□ Setup media storage (S3)
□ Add monitoring (Sentry)
□ Configure backups
□ Setup CI/CD
□ Add rate limiting
□ Security audit


╔══════════════════════════════════════════════════════════════════════════════╗
║                          END OF FLOW DIAGRAM                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

if __name__ == '__main__':
    print_diagram()
