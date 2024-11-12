from flask import Flask,render_template,request,redirect,url_for,flash
from flask_login import login_user,logout_user,LoginManager,current_user,login_required
from sqlalchemy import or_
import matplotlib.pyplot as plt
from graph import *
from models import *

#========================================CONFIGURATION=====================================================================
app = Flask(__name__)
login_manager=LoginManager()
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///satish.sqlite'
app.app_context().push()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
db.init_app(app)

############################################CONTROLLERS############################################################
#==========================================HOME=====================================================================

@app.route('/')
def home():
    return render_template("home.html")

#==========================================LOGIN=====================================================================

@app.route("/login" ,  methods =["GET", "POST"])
def login():
    if request.method == "GET" :
        return render_template("login.html")
    if request.method == "POST" :
        password=request.form["password"]
        email=request.form["email"]

        user = User.query.filter_by(email=email).first()
        if user is None :
            error = "Account Not Found, Please Register First!!"
            return render_template("login.html",error=error)
            
        
        if user.password != password :
            error = "Invalid Credentials"
            return render_template("login.html",error=error)
        
        else :
            accounts=db.session.query(User).filter(User.email==email, User.password==password ).first()
            if (db.session.query(User).filter(User.email==email, User.password==password,User.role =='User').first()):
                login_user(accounts)
                return redirect("/dashboard")
                    
            elif(db.session.query(User).filter(User.email==email, User.password==password,User.role =='creator').first()):
                login_user(accounts)
                return redirect("/creator_dashboard")
            elif(db.session.query(User).filter(User.email==email, User.password==password,User.role =='admin').first()):
                error = "Invalid Credentials"
                return render_template("login.html",error=error)

#==========================================LOGOUT=====================================================================

@app.route('/logout')
@login_required

def logout():
    #print(f'{current_user.username}')
    logout_user()
    return redirect("/")
        
#==========================================REGISTER=====================================================================

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")

    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        u = User(email=email, password=password, username=username)
        
        existing_user = db.session.query(User).filter(User.email == email).first()
        existing_username = db.session.query(User).filter(User.username == username).first()
        
        if existing_user or existing_username:
            if existing_user:
                error = "Email ID Already exists"
            else:
                error="Username already exists"
            return render_template("register.html", error=error)
        
        else:
            db.session.add(u)
            db.session.commit()
            return redirect(url_for('login'))
  
#==========================================DASHBOARD=====================================================================

@app.route('/dashboard')
def dashboard():
    user=current_user
    flash("logged in successfully","success")
    song = Song.query.filter_by(flagged=False).all()
    return render_template("dashboard.html",song=song, user=user)

#==========================================LYRICS=====================================================================

@app.route('/lyrics/<int:id>')
def lyrics(id):
    user=current_user
    song=Song.query.all()
    c=Song.query.get(id)
    return render_template('lyrics.html',song=song,c=c, user=user)

#==========================================CREATE PLAYLIST=====================================================================

@app.route('/create_playlist', methods=['GET', 'POST'])
def create_playlist():
    # checking user (particular user ki particular playlist)
    user = current_user
    if request.method == 'GET':
        return render_template("create_playlist.html", user=user)
    if request.method == 'POST':
        name = request.form.get('name')

        # Check kiye already hai kya playlist
        existing_playlist = Playlist.query.filter_by(name=name, user_id=user.id).first()

        if existing_playlist:
            error = f"Playlist with {name} name already exist, please choose a different name for playlist"
            return render_template("create_playlist.html",error=error,user=current_user)
        
        new_playlist = Playlist(name=name, user_id=user.id)
        db.session.add(new_playlist)
        db.session.commit()
        return redirect('/your_playlist')

    
#==========================================YOUR PLAYLIST=====================================================================

@app.route('/your_playlist')
def your_playlist():
    user = current_user
    playlist = Playlist.query.filter_by(user_id=user.id).all()
    return render_template("your_playlist.html", playlist=playlist, user=user)


#==========================================ADD SONGS TO PLAYLIST=====================================================================

@app.route('/add_songs/<int:id>', methods=['GET','POST'])
def add_songs(id):
    if request.method== 'GET':
        user=current_user
        #song= Song.query.all()
        song = Song.query.filter_by(flagged=False).all()
        playlist = Playlist.query.all()
        p = Playlist.query.get(id)
        return render_template('add_songs.html',song=song,playlist=playlist,p=p)
    if request.method == 'POST':
        s = request.form['song_id']
        p = Playlist.query.get(id)
        song= Song.query.get(s)
        try:
            p.songs.append(song)
            db.session.commit()
        except:
            return "Song Already Added <h3><a href=/your_playlist> Go Back </a><h3>"

        return redirect(url_for('your_playlist'))
    
#==========================================PLAYLIST SONGS=====================================================================

@app.route("/playlist_song/<int:id>")
def playlist_song(id):
    song=Song.query.all()
    p=Playlist.query.filter_by(id=id).first()
    return render_template("playlist_song.html",song=song,p=p)
            
#==========================================CREATOR REGISTRATION=====================================================================

@app.route('/creator_registration')
def creator_registration():
    if request.method =="GET":
        user=current_user
        user.role='creator'
        db.session.commit()
        return redirect("/creator_dashboard")
    
#==========================================CREATOR DASHBOARD=====================================================================

@app.route('/creator_dashboard')
def creator_dashboard():
    user=current_user
    song = Song.query.filter_by(flagged=False).all()
    #print(song)
    return render_template('creator_dashboard.html', song=song, user=user)

#==========================================EDIT PLAYLIST =====================================================================

@app.route('/edit_playlist/<int:playlist_id>', methods=['GET', 'POST'])
def edit_playlist(playlist_id):
    user=current_user
    playlist = Playlist.query.get(playlist_id)

    if request.method == 'POST':

        new_name = request.form['new_name']
        existing_playlist = Playlist.query.filter_by(name=new_name, user_id=user.id).first()
        if existing_playlist:
            error = f"Playlist with {new_name} name already exist, please choose a different name for Playlist"
            return render_template("edit_playlist.html",error=error, playlist=playlist)
        
        playlist.name = new_name
        db.session.commit()
        return redirect(url_for('your_playlist'))

    return render_template('edit_playlist.html', playlist=playlist)

#==========================================DELETE PLAYLIST=====================================================================

@app.route('/delete_playlist/<int:playlist_id>')
def delete_playlist(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    db.session.delete(playlist)
    db.session.commit()
    return redirect(url_for('your_playlist'))

#==========================================DELETE SONG FROM PLAYLIST =====================================================================

@app.route('/delete_song/<int:playlist_id>/<int:song_id>')
def delete_song(playlist_id, song_id):
    playlist = Playlist.query.get(playlist_id)
    song = Song.query.get(song_id)

    playlist.songs.remove(song)
    db.session.commit()

    return redirect(url_for('playlist_song', id=playlist_id))

#==========================================CREATE ALBUM=====================================================================

@app.route('/create_album', methods=['GET','POST'])
def create_album():
    user = current_user
    if request.method == 'GET':
        return render_template("create_album.html")
    
    if request.method == 'POST':
        name = request.form.get('name')
        #album = Album.query.all()
        existing_album = Album.query.filter_by(name=name, user_id=user.id).first()
        
        if user.blacklisted:
            error="You are blacklisted. You cannot add any album until you gets whitelisted."
            #print("12345")
            return render_template("create_album.html",error=error)



        elif existing_album:
            error = f"Album with {name} name already exist, please choose a different name for album"
            return render_template("create_album.html",error=error)
        
        c = Album(name=name, user_id=user.id)
        db.session.add(c)
        db.session.commit()
        return redirect('/your_album')

#==========================================YOUR ALBUM=====================================================================

@app.route('/your_album')
def your_album():
    user = current_user
    album = Album.query.filter_by(user_id=user.id).all()
    return render_template("your_album.html", album=album, user=user)
    
#==========================================ADD SONGS TO ALBUM=====================================================================

@app.route('/add_album_songs/<int:id>', methods=['GET','POST'])
def add_album_songs(id):
    user=current_user
    if request.method== 'GET':
        song= Song.query.filter_by(us_id=user.id).all()
        #s = Song.query.get(id)
        album = Album.query.all()
        a = Album.query.get(id)
        return render_template('add_album_songs.html',song=song,album=album,a=a,user=user)
    if request.method == 'POST':
        s = request.form['song_id']
        a = Album.query.get(id)
        song= Song.query.get(s)
        try:
            a.songs.append(song)
            db.session.commit()
        except:
            return "Song Already Added <h3><a href=/your_album> Go Back </a><h3>"        
        return redirect('/your_album')
    
#==========================================ALBUM SONGS=====================================================================
    
@app.route("/album_song/<int:id>")
def album_song(id):
    song=Song.query.all()
    a=Album.query.filter_by(id=id).first()
    return render_template("album_song.html",song=song,a=a)

#==========================================EDIT ALBUM=====================================================================

@app.route('/edit_album/<int:album_id>', methods=['GET', 'POST'])
def edit_album(album_id):
    album = Album.query.get(album_id)
    user=current_user

    if request.method == 'POST':

        new_name = request.form['new_name']
        existing_album = Album.query.filter_by(name=new_name, user_id=user.id).first()
        if existing_album:
            error = f"Album with {new_name} name already exist, please choose a different name for album"
            return render_template("edit_album.html",error=error,album=album)
        album.name = new_name
        db.session.commit()
        return redirect(url_for('your_album'))

    return render_template('edit_album.html', album=album)

#==========================================DELETE ALBUM=====================================================================

@app.route('/delete_album/<int:album_id>')
def delete_album(album_id):
    album = Album.query.get(album_id)
    db.session.delete(album)
    db.session.commit()
    return redirect(url_for('your_album'))

#==========================================DELETE SONG FROM ALBUM =====================================================================

@app.route('/delete_album_song/<int:album_id>/<int:song_id>')
def delete_album_song(album_id, song_id):
    album = Album.query.get(album_id)
    song = Song.query.get(song_id)

    album.songs.remove(song)
    db.session.commit()

    return redirect(url_for('album_song', id=album_id))

#==========================================UPLOAD A SONG AS CREATOR =====================================================================

@app.route('/upload_song', methods=['GET', 'POST'])
def add_song():
    if request.method == 'GET':
        return render_template('upload_song.html')

    if request.method == 'POST':
        user=current_user
        song_name = request.form['song_name']
        artist = request.form['artist']
        genre = request.form['genre']
        lyrics = request.form['lyrics']
        
        if user.blacklisted:
            error="You are blacklisted. You cannot Upload any Song until you gets whitelisted."
            #print("12345")
            return render_template("upload_song.html",error=error)

        else:
            new_song = Song(song_name=song_name, artist=artist, genre=genre, lyrics=lyrics, ratings=0.0, us_id=current_user.id)
            db.session.add(new_song)
            db.session.commit()

            return redirect(url_for('uploaded_songs'))

#==========================================UPDATE A SONG(CREATOR) =====================================================================

@app.route('/update_song/<int:id>', methods=['GET', 'POST'])
def update_song(id):
    s = Song.query.get(id)
    if request.method == 'GET':
        return render_template('update_song.html',s=s)
    if request.method == 'POST':
        # Update the song name
        new_name = request.form['new_name']
        new_lyrics = request.form['new_lyrics']
        s.song_name = new_name
        s.lyrics = new_lyrics
        db.session.commit()
        return redirect(url_for('uploaded_songs'))
    
#==========================================UPLOADED SONGS(CREATOR) =====================================================================
@app.route('/uploaded_songs')
def uploaded_songs():
    user = current_user
    song=Song.query.filter_by(us_id=user.id).all()
    return render_template("uploaded_songs.html",user=user, song=song)

#==========================================DELETE SONG(CREATOR) =====================================================================

@app.route('/delete_creator_song/<int:song_id>')
def delete_creator_song(song_id):
    song = Song.query.get(song_id)
    db.session.delete(song)
    db.session.commit()
    return redirect(url_for('uploaded_songs'))

#==========================================ALL ALBUM =====================================================================

@app.route('/all_album/')
def all_album():
    user1=current_user
    user = User.query.all()
    album = Album.query.all()
    return render_template('all_album.html', album=album, user=user, user1=user1)

#==========================================ALL ALBUM SONG =====================================================================

@app.route('/all_album_songs/<int:album_id>')
def all_album_songs(album_id):
    album = Album.query.get(album_id)
    songs = Song.query.all()
    return render_template('all_album_songs.html', album=album, songs=songs)


#==========================================RATING SONGS =====================================================================

@app.route('/rate_song/<int:song_id>', methods=['POST'])
def rate_song(song_id):
    user = current_user
    rating_value = int(request.form.get('rating'))

    user_id = current_user.id
    existing_rating = Rating.query.filter_by(user_id=user_id, song_id=song_id).first()

    if existing_rating:
        existing_rating.rating = rating_value
    else:
        new_rating = Rating(user_id=user_id, song_id=song_id, rating=rating_value)
        db.session.add(new_rating)
    song = Song.query.get(song_id)
    if song.ratings_count is None:
        song.ratings_count = 0

    song.ratings_total += rating_value
    song.ratings_count += 1
    song.ratings = round((song.ratings_total / song.ratings_count),1)
    db.session.commit()
    if user.role == "User":
        return redirect(url_for('dashboard'))
    else :
        return redirect(url_for('creator_dashboard'))
   
#==========================================ADMIN LOGIN=====================================================================
    
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('admin_login.html')

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, role='admin').first()

        if user and user.password == password:
            pie_chart()
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            error = "Invalid email or password"
            return render_template('admin_login.html', error=error)


#==========================================ADMIN DASHBOARD=====================================================================
  
@app.route('/admin_dashboard')
def admin_dashboard():
    user=current_user
    user = User.query.all()
    song = Song.query.all()
    u_count = len(User.query.filter_by(role ="User").all())
    c_count = len(User.query.filter_by(role ="creator").all())
    blcr_count = len(User.query.filter_by(blacklisted = True).all())
    song_count =len(song)
    fls_count = len(Song.query.filter_by(flagged = True).all())
    top_songs = Song.query.order_by(Song.ratings.desc()).limit(5).all()
    
    return render_template("admin_dashboard.html",user=user,u_count=u_count, c_count=c_count, song_count=song_count, top_songs=top_songs, blcr_count=blcr_count, fls_count=fls_count)

#==========================================ADMIN SONG MANAGEMENT=====================================================================
  
@app.route('/admin_songs_man')
def admin_songs_man():
    song=Song.query.all()
    return render_template("admin_songs_man.html",song=song)

#==========================================FLAGGING SONGS=====================================================================

@app.route('/flag_song/<int:song_id>', methods=['POST'])
def flag_song(song_id):
    action = request.form.get('flagsong')
    song = Song.query.get(song_id)

    if song:
        if action == 'flag':
            song.flagged = True
        elif action == 'unflag':
            song.flagged = False

        db.session.commit()

    return redirect(url_for('admin_songs_man'))

#==========================================ADMIN DELETING SONGS=====================================================================

@app.route('/admin_del_song/<int:id>')
def admin_del_song(id):
    song = Song.query.get(id)
    db.session.delete(song)
    db.session.commit()

    return redirect(url_for('admin_songs_man'))

#==========================================ADMIN USER MANAGEMENT=====================================================================
  
@app.route('/admin_user_man')
def admin_user_man():
    user=User.query.all()
    return render_template("admin_user_man.html",user=user)

#==========================================BLACKLISTING USERS=====================================================================

@app.route('/black_user/<int:user_id>', methods=['POST'])
def black_user(user_id):
    action = request.form.get('blackuser')
    user = User.query.get(user_id)

    if user:
        if action == 'blacklist':
            user.blacklisted = True

            songs_flag_after_black = Song.query.filter_by(us_id=user.id).all()
            for song in songs_flag_after_black:
                song.flagged = True

        elif action == 'whitelist':
            user.blacklisted = False

            songs_unflag_after_black = Song.query.filter_by(us_id=user.id).all()
            for song in songs_unflag_after_black :
                song.flagged = False

        db.session.commit()

    return redirect(url_for('admin_user_man'))


#========================================== SEARCH =====================================================================

@app.route("/search" , methods=["GET" , "POST"])
def search():
    query = request.form['query']
    query = f"%{query}%"
    
    results = Song.query.filter( or_(
                    Song.song_name.contains(query),
                    Song.artist.contains(query),
                    Song.genre.contains(query))).all()
    user=current_user
    song = Song.query.filter_by(flagged=False).all()
    if(user.role=="User"):
        return render_template("dashboard.html",song=song, user=user,results=results)
    elif(user.role=="creator"):
        return render_template('creator_dashboard.html', song=song, user=user,results=results)
    elif(user.role=="admin"):
        return render_template('admin_songs_man.html', song=song, user=user,results=results)

#========================================== ADMIN SEEING SONGS OF PARTICULAR USER =====================================================================

@app.route('/admin_creator_songs/<int:user_id>')
def admin_creator_songs(user_id):
    song=Song.query.filter_by(us_id=user_id).all()
    return render_template("admin_creator_songs.html", song=song)

#========================================== PLAY SONG :) =====================================================================
@app.route('/play')
def play():
    return render_template("play.html")

if __name__ == '__main__':
    app.run(debug=True)
