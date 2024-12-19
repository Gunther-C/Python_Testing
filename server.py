import os
import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'something_special'


def load_clubs():
    try:
        path_club = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path_club, 'clubs.json')) as _clubs:
            list_clubs = json.load(_clubs)['clubs']
            return list_clubs
    except (FileNotFoundError, json.JSONDecodeError):  # pragma: no cover
        return []  # pragma: no cover


def load_competitions():
    try:
        path_competition = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path_competition, 'competitions.json')) as comps:
            list_competitions = json.load(comps)['competitions']
            return list_competitions
    except (FileNotFoundError, json.JSONDecodeError):  # pragma: no cover
        return []  # pragma: no cover


app.clubs = load_clubs()
app.competitions = load_competitions()


def find_entity(entities, value, entity_type, search_type):
    entity = [ent for ent in entities if ent[search_type] == value]
    if not entity:
        flash(f"No {entity_type} found with the provided {search_type}.")
        return None
    return entity[0]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show_summary', methods=['POST'])
def show_summary():
    club = find_entity(app.clubs, request.form['email'], 'club', 'email')
    if club is None:
        return redirect(url_for('index'))

    return render_template('welcome.html', club=club, competitions=app.competitions,
                           datetime=datetime)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = find_entity(app.clubs, club, 'club', 'name')
    if found_club is None:
        return redirect(url_for('index'))

    found_competition = find_entity(app.competitions, competition, 'competition', 'name')
    if found_competition is None:
        return render_template('welcome.html', club=found_club, competitions=app.competitions,
                               datetime=datetime)

    competition_date = datetime.strptime(found_competition['date'], "%Y-%m-%d %H:%M:%S")
    if competition_date < datetime.now():
        flash(f"This competition {found_competition['name']} has already taken place.")
        return render_template('welcome.html', club=found_club, competitions=app.competitions,
                               datetime=datetime)

    max_places = min(12, int(found_club['points']), int(found_competition['numberOfPlaces']))

    return render_template('booking.html',
                           club=found_club, competition=found_competition, max_places=max_places)


@app.route('/purchase_places', methods=['POST'])
def purchase_places():
    club = find_entity(app.clubs, request.form['club'], 'club', 'name')
    if club is None:
        return redirect(url_for('index'))

    competition = find_entity(app.competitions, request.form['competition'], 'competition', 'name')
    if competition is None:
        return render_template('welcome.html', club=club, competitions=app.competitions,
                               datetime=datetime)

    places_required = int(request.form['places'])

    if places_required > int(club['points']):
        flash("Not enough points available.")
        return render_template('booking.html', club=club, competition=competition)

    if places_required > int(competition['numberOfPlaces']):
        flash(f"Booking limit of {competition['numberOfPlaces']} places.")
        return render_template('booking.html', club=club, competition=competition)

    if places_required > 12:
        flash("Booking limit of 12 places exceeded.")
        return render_template('booking.html', club=club, competition=competition)

    competition['numberOfPlaces'] = str(int(competition['numberOfPlaces']) - places_required)
    club['points'] = str(int(club['points']) - places_required)

    flash("Great - booking complete! You have booked place(s).")

    return render_template('welcome.html', club=club, competitions=app.competitions,
                           datetime=datetime)


@app.route('/show_clubs')
def show_clubs():
    if not app.clubs:
        flash("No registered club.")
        return redirect(url_for('index'))

    clubs_list = sorted(app.clubs, key=lambda x: x['points'], reverse=True)
    return render_template('clubs.html', clubs=clubs_list)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
