# WE-ICT 2026 Backend API

Registration system backend for the Women Empowerment through ICT Workshop 2026.

## PythonAnywhere Deployment Guide

### Step 1: Create Account
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up for a free "Beginner" account
3. Verify your email

### Step 2: Upload Files
1. Go to **Files** tab
2. Create folder: `workshop-backend`
3. Upload all files from `/backend` folder
4. Create a `.env` file with your actual credentials

### Step 3: Install Dependencies
1. Go to **Consoles** → **Bash**
2. Navigate: `cd workshop-backend`
3. Install packages: `pip3 install --user -r requirements.txt`

### Step 4: Configure Web App
1. Go to **Web** tab
2. Click "Add a new web app"
3. Choose **Flask** framework
4. Python version: **3.10**
5. Path to Flask app: `/home/YOUR-USERNAME/workshop-backend/app.py`

### Step 5: WSGI Configuration
1. In Web tab, click on WSGI configuration file link
2. Replace content with:
```python
import sys
path = '/home/YOUR-USERNAME/workshop-backend'
if path not in sys.path:
    sys.path.append(path)

from app import app as application

