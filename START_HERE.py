"""
Quick Start Script - Run this first!
"""
import os
import sys

def main():
    print("=" * 60)
    print(" " * 15 + "SKILL SWAP PLATFORM")
    print(" " * 15 + "Quick Start Guide")
    print("=" * 60)
    print()
    
    print("This script will help you set up the Skill Swap platform.")
    print()
    
    print("📋 What you need:")
    print("   ✓ Python 3.8+")
    print("   ✓ Virtual environment (already created)")
    print("   ✓ Internet connection (for packages)")
    print()
    
    print("🚀 Setup Steps:")
    print()
    print("   1️⃣  Run: python build_project.py")
    print("       Creates all Django apps and files")
    print()
    print("   2️⃣  Run: python build_templates.py")
    print("       Creates all HTML templates")
    print()
    print("   3️⃣  Activate venv: venv\\Scripts\\activate")
    print("       Activates your virtual environment")
    print()
    print("   4️⃣  Install: pip install -r requirements.txt")
    print("       Installs Django, Channels, etc.")
    print()
    print("   5️⃣  Migrate: python manage.py makemigrations")
    print("               python manage.py migrate")
    print("       Sets up the database")
    print()
    print("   6️⃣  Create admin: python manage.py createsuperuser")
    print("       Creates your admin account")
    print()
    print("   7️⃣  Run server: python manage.py runserver")
    print("       Starts the development server")
    print()
    
    print("=" * 60)
    print()
    print("💡 EASY MODE: Just run 'complete_setup.bat'")
    print("   This will do steps 1-5 automatically!")
    print()
    print("=" * 60)
    print()
    
    choice = input("Do you want to see the file structure? (y/n): ")
    if choice.lower() == 'y':
        print()
        print("📁 File Structure:")
        print("""
skill_swap/
│
├── 📄 manage.py
├── 📄 requirements.txt
├── 📄 complete_setup.bat          ← Run this!
├── 📄 build_project.py
├── 📄 build_templates.py
├── 📄 README.md
├── 📄 SETUP_GUIDE.md
├── 📄 PROJECT_SUMMARY.md
│
├── 📁 skill_swap/                 (Settings)
├── 📁 users/                      (Login, Profile, Skills)
├── 📁 dashboard/                  (Main Interface)
├── 📁 chat/                       (Real-time Chat)
├── 📁 video/                      (Video Calls)
├── 📁 templates/                  (Base Templates)
├── 📁 static/                     (CSS, JS)
├── 📁 media/                      (Uploads)
└── 📁 venv/                       (Python Environment)
        """)
    
    print()
    print("=" * 60)
    print("Ready to start? Run: complete_setup.bat")
    print("=" * 60)
    print()

if __name__ == '__main__':
    main()
