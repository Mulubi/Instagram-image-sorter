from flask import render_template, url_for, session, redirect, flash, request, jsonify
import requests
import time
from pymongo import MongoClient
from datetime import datetime, date
from . import main
# from .forms import RegistrationForm, LoginForm, TheatreForm, DashboardForm, TheatreAddForm
# from .. import db, bcrypt
# from models import User
# from Flask_BMT.models.users import User
# from Flask_BMT.models.theatres import TheatreList
# from flask_login import login_required, login_user, logout_user, current_user
# from Flask_BMT.main.decorator import admin_required, permission_required

from instagrapi import Client

cl = Client()
ACCOUNT_USERNAME = ""
ACCOUNT_PASSWORD = ""
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)



@main.route('/')
@main.route('/home')
def home_page():
    return "This is the home page, Mr Wice"

# Initialize MongoDB client (you need to set up MongoDB separately)
# client = MongoClient('mongodb://localhost:27017/')
#db = client['instagram_viewer']
#users_collection = db['users']
#marked_images_collection = db['marked_images']

# Your Instagram private API functions go here
def fetch_images_from_instagram(username):
    # Implement logic to fetch images using private API
    try:
        user_id = cl.user_id_from_username(username)
        # medias = cl.user_medias(user_id, 12)

        end_cursor = None
        media_per_page = 12

        for page in range(3):
            medias, end_cursor = cl.user_medias_paginated(user_id, media_per_page, end_cursor=end_cursor)

            for media in medias:
                print("Media ID:", media.pk)
                print("Caption:", media.caption_text)
                print("Media Type:", media.media_type)
                print("Taken At:", media.taken_at.date().isoformat)
                print("")

            if not end_cursor:
                break
    except Exception as e:
        print(f"An error occurred while getting the images: {str(e)}")
        return None

    return None

# Define routes

# Route to fetch and display images for a user
@main.route('/api/v1/users/<username>')
def display_user_images(username):
    # user_data = users_collection.find_one({'username': username})
    # if not user_data:
    #     return jsonify({'error': 'User not found'}), 404

    # Fetch images from Instagram using your private API function
    images = fetch_images_from_instagram(username)

    if images:
        for image in images:
            print(f"Image URL: {image['url']}")

    return jsonify(images)

# Route to mark an image
@main.route('/mark/<username>/<image_id>', methods=['POST'])
def mark_image(username, image_id):
    # Log the marked image in the database with a timestamp
    # marked_images_collection.insert_one({
    #     'username': username,
    #     'image_id': image_id,
    #     'timestamp': int(time.time())
    # })
    return jsonify({'message': 'Image marked successfully'})

# Route to pause image rotation
@main.route('/pause/<username>', methods=['POST'])
def pause_rotation(username):
    # Implement logic to pause image rotation
    pass

# Route to go back to the previous image
@main.route('/back/<username>', methods=['POST'])
def go_back(username):
    # Implement logic to navigate to the previous image
    pass
