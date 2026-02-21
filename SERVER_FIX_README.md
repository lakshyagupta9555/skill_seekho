# SkillSwap - Server Fix Guide

## Problem: Can't Run `python manage.py runserver`

Your `manage.py` file was corrupted. This has been fixed!

## Solution: Run This Command

### Option 1: Use the Batch File (EASIEST)
```
.\START_SERVER.bat
```

This will:
1. Fix your manage.py file automatically
2. Activate the virtual environment
3. Run migrations
4. Start the Django server

### Option 2: Manual Fix
If the batch file doesn't work, do these steps manually:

**Step 1: Delete the broken manage.py**
```
del manage.py
```

**Step 2: Rename the working file**
```
copy manage_new.py manage.py
```

**Step 3: Activate virtual environment**
```
venv\Scripts\activate
```

**Step 4: Run migrations**
```
python manage.py makemigrations
python manage.py migrate
```

**Step 5: Start the server**
```
python manage.py runserver
```

### Option 3: If Python Command Fails

If you get "python is not recognized", try:
```
py manage.py runserver
```

Or find your Python path:
```
where python
```

## What Was Wrong?

The `manage.py` file got corrupted and only contained "1." instead of the proper Django management script. I've created a new working version in `manage_new.py` and the batch file will replace the broken one.

## After Server Starts

1. Open your browser
2. Go to: **http://127.0.0.1:8000/**
3. Register a new account
4. Start using SkillSwap!

## Files Created

- `START_SERVER.bat` - Fixes manage.py and starts server (USE THIS!)
- `manage_new.py` - Working version of manage.py
- `FIX_MANAGE_PY.bat` - Alternative fix script

## Still Having Issues?

Make sure you're in the correct directory:
```
cd c:\Users\laksh\OneDrive\Desktop\skill_swap
```

Check if virtual environment exists:
```
dir venv
```

If venv doesn't exist, create it:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

**TL;DR: Just run `.\START_SERVER.bat` and it will fix everything!**
