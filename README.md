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

![Screenshot 1](https://github.com/user-attachments/assets/9146f1dd-bde7-42a6-8f7a-2e01d850cb45)
![Screenshot 2](https://github.com/user-attachments/assets/f683d617-e46f-44bb-8434-9b261650537c)
![Screenshot 3](https://github.com/user-attachments/assets/944f2a41-90ce-41dd-860b-a8d200ffca85)

## Video
Check out the video demonstration of the Sargam project here: [Video Link](Video Link)

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
1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd sargam
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up the database**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```
5. **Run the development server**:
   ```bash
   flask run
   ```

---

This README file provides a complete overview of the Sargam app, its features, technologies, database schema, architecture, and instructions for setup, aimed to help users and contributors understand and navigate the project effortlessly.
