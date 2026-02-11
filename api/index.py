from app import app

# Vercel's Python runtime looks for a WSGI-compatible object named `app`.
# Importing from the root `app.py` exposes the existing Flask instance.
