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

![Screenshot (508)](https://github.com/user-attachments/assets/c51a7a79-ea35-4bf9-9ccc-b509a932e111)
![Screenshot (509)](https://github.com/user-attachments/assets/87134a26-dd65-4158-ac3b-be5cd3036211)
![Screenshot (510)](https://github.com/user-attachments/assets/45fc8563-035e-4ee6-9683-44fe3ab6350b)
![Screenshot (511)](https://github.com/user-attachments/assets/75a4c885-7295-44f2-a030-eb6e161e618d)
![Screenshot (512)](https://github.com/user-attachments/assets/ab30f2f2-5c04-4fc1-b6e2-fea9c7606a35)
![Screenshot (513)](https://github.com/user-attachments/assets/d645b7f5-5021-4290-9309-811910bb11eb)

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
