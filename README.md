# Sargam

**Welcome to Sargam**, a lightweight and intuitive music platform designed for music lovers and creators. Sargam allows you to explore a diverse range of songs, view lyrics, learn about artists and genres, and rate your favorite tracks for a personalized musical experience.

## Features
- **Song Discovery**: Find and enjoy songs across various genres with easy-to-use search functionality.
- **Lyrics and Artist Info**: View lyrics and learn about the artists behind the music.
- **Personalized Playlists**: Create and organize playlists tailored to your mood or occasion.
- **Creator Hub**: Upload your own songs and release albums, empowering you to share your music.
- **User & Admin Roles**: Secure login for users and admins, with separate portals for each role.
- **CRUD Operations**: Full control over song, playlist, and album management, with CRUD features for admins and creators.
- **Rating System**: Rate songs based on your preferences and keep track of your favorites.
- **Data Visualization**: View musical insights through dynamic charts and graphs using Matplotlib.

## Screenshots
![Screenshot (508)](https://github.com/user-attachments/assets/5b5c241b-6b23-421e-abf8-83d822fc57a0)
![Screenshot (509)](https://github.com/user-attachments/assets/02cf71aa-06a7-4156-86a2-0addef8b0489)
![Screenshot (510)](https://github.com/user-attachments/assets/96b68c54-884a-431b-9ba2-112f46eca0f6)
![Screenshot (511)](https://github.com/user-attachments/assets/82cf690b-5477-401d-9dd5-58e25f4cb826)
![Screenshot (512)](https://github.com/user-attachments/assets/333a0093-bd39-417f-9138-b0bb8a76c9d4)
![Screenshot (513)](https://github.com/user-attachments/assets/dde3fa5e-6924-4ca8-8765-60d1336c7395)

## Technologies Used

### Backend
- **Flask**: Web framework for backend development.
- **Flask-Login**: User session management and authentication.
- **Flask-SQLAlchemy**: Database management with SQLAlchemy ORM.
- **SQLAlchemy**: Object-relational mapping for database interaction.
- **Matplotlib**: Data visualization for charts and graphs.

### Frontend
- **HTML, CSS, Bootstrap**: User interface design and styling.
- **Jinja**: Template engine for rendering dynamic content.

## Database Schema Design
The database schema for Sargam includes the following tables:
- **User**: Stores user details like username, email, role, and playlists.
- **Song**: Contains song details, ratings, and flags for management.
- **Playlist**: Stores user-created song collections.
- **Album**: Manages collections of songs created by users.
- **Rating**: Tracks user ratings for songs.

This schema supports interactions between users, songs, playlists, and albums, providing a foundation for an engaging and organized music experience.

## Architecture and Files

### Root Folder Contains:
- **app.py**: Acts as the main controller, defining routes and managing API endpoints.
- **models.py**: Defines database models for users, songs, playlists, and albums.
- **graph.py**: Generates visualizations for data insights using Matplotlib.
- **readme.md**: Project overview and setup instructions.
- **requirements.txt**: Lists project dependencies.
- **instance folder**: Contains the SQLite database file.
- **templates folder**: Stores HTML and CSS files.
- **static folder**: Contains static assets, such as images and audio files.

### Detailed Files:
- **app.py**: Manages routes to different pages and defines user roles and permissions.
- **models.py**: Manages database models for a seamless user and admin experience.
- **graph.py**: Creates dynamic visualizations to represent user interactions with music content.

## Installation and Setup
# Getting Started
### Prerequisites
To run Music Streaming App on your local device, you will need to have the following installed:

- Python 3
- Pip

### Installation
Install the required packages
```
pip install -r requirements.txt
```
start the app

```
flask run
```
### DataBase Creation
flask shell
```
db.create_all()
exit()
```
### Usage
Register for an account if you are new or login if you already have one.
Once logged in, you can create playlists,become a creator, can create your albumns, give ratings etc.

---

This README file provides a complete overview of the Sargam app, its features, technologies, database schema, architecture, and instructions for setup, aimed to help users and contributors understand and navigate the project effortlessly.
