from flask_sqlalchemy import SQLAlchemy

#from flask_migrate import Migrate

from flask import Flask

app=Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.PickleType())
    website_link = db.Column(db.String(200))
    seeking_talent = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(500))
    #------------Lier Artist
    artists = db.relationship('Artist', secondary='shows')
    def __repr__(self):
        return f'<Venue {self.id} {self.name} {self.city} >'

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.PickleType())
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website_link = db.Column(db.String(200))
    seeking_venue = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(500))
    #--------------------Lier Venue
    venues = db.relationship('Venue', secondary='shows')
    def __repr__(self):
        return f'<Artist: {self.id} {self.name} {self.city} {self.genres}>'

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration. 

class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    venue_id =  db.Column(db.Integer, db.ForeignKey('venues.id'))
    artist_id =  db.Column(db.Integer, db.ForeignKey('artists.id'))
    start_time = db.Column(db.DateTime, nullable = False)

    #----------------lier artist et venue
    venues = db.relationship('Venue', backref = db.backref('venues', lazy = True))
    artists = db.relationship('Artist', backref = db.backref('artists', lazy = True))

    def __repr__(self):
        return f'<Show: {self.id} {self.venue_id} {self.artist_id} {self.start_time}>'