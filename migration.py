import json
import requests
from app import db

# 🔹 JSON Data to be Uploaded
data = {
    "Achivements": {
        "First Achivements": {
            "author": "thisjpsingh@gmail.com",
            "date": "12-03-2025",
            "link": "https://github.com/v9dev",
            "name": "Jitendra Pratap Singh",
            "profile_pic": "https://res.cloudinary.com/dymm4ewoc/image/upload/v1741723579/f5dmvd5vcdfhet6dby8l.jpg",
            "title": "First Achivements",
            "user_title": "Full Stack Developer"
        }
    },
    "users": {}
}

# 🔹 Upload JSON Data to Firebase
db.update(data)
print("✅ Data added successfully!")