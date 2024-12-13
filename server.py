import os
import json
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'something_special'


def load_clubs():
    try:
        path_club = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path_club, 'clubs.json')) as _clubs:
            list_clubs = json.load(_clubs)['clubs']
            return list_clubs
    except:
        return []


def load_competitions():
    try:
        path_competition = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path_competition, 'competitions.json')) as comps:
            list_competitions = json.load(comps)['competitions']
            return list_competitions
    except:
        return []


app.clubs = load_clubs()
app.competitions = load_competitions()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show_summary', methods=['POST'])
def show_summary():
    club = [_club for _club in app.clubs if _club['email'] == request.form['email']]
    if not club:
        flash("No club found with the provided email address.")
        return redirect(url_for('index'))
    return render_template('welcome.html', club=club[0], competitions=app.competitions)

@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))