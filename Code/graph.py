from flask import Flask,render_template,request,redirect,url_for,flash
from flask_login import login_user,logout_user,LoginManager,current_user
import matplotlib.pyplot as plt
from models import *

def pie_chart():
    query01 = Song.query.filter(Song.ratings.between(0.0,1.0)).all()
    query12 = Song.query.filter(Song.ratings.between(1.0,2.0)).all()
    query23 = Song.query.filter(Song.ratings.between(2.0,3.0)).all()
    query34 = Song.query.filter(Song.ratings.between(3.0,4.0)).all()
    query45 = Song.query.filter(Song.ratings.between(4.0,5.0)).all()
    d = {'Rating(0-1)': 0, 'Rating(1-2)': 0, 'Rating(2-3)': 0, 'Rating(3-4)': 0, 'Rating(4-5)': 0}
    d['Rating(0-1)']=len(query01)
    d['Rating(1-2)']=len(query12)
    d['Rating(2-3)']=len(query23)
    d['Rating(3-4)']=len(query34)
    d['Rating(4-5)']=len(query45)
    labels=d.keys()
    values=d.values()
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal') 
    plt.title("Piechart for Song Ratings")
    # plt.show()
    plt.savefig('C:/Users/satis/Desktop/MAD1_APP/static/piechart.png')

    plt.clf()
    