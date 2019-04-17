#__author__ == "Chenrui Shu(crshu)"

import os
from flask import Flask, render_template, redirect, url_for, request 
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from SI507project_tools import *



# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=0.5)

# Set up Flask debug stuff for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./parks.db' 
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy


##### Set up Models #####


class State(db.Model):
    __tablename__ = 'state' # special variable useful for referencing in other/later code
    # Here we define columns for the table
    # Notice that each column is also basically a class variable
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # autoincrements by default
    name = db.Column(db.String(250), nullable=False) 
 
    def __repr__(self):
        return "state: {}".format(self.name)

class Type(db.Model):
    __tablename__ = 'type' # special variable useful for referencing in other/later code
    # Here we define columns for the table
    # Notice that each column is also basically a class variable
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # autoincrements by default
    name = db.Column(db.String(250), nullable=False) 

    def __repr__(self):
        return "type: {}".format(self.name)

class Park(db.Model):
    __tablename__ = 'park'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(500))
    location = db.Column(db.String(250))
    pysical_address = db.Column(db.String(250))
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))
    state = db.relationship("State", backref="parks")
    type = db.relationship("Type", backref = "parks")


    def __repr__(self):
        return "{} in {} state wity type {}".format(self.name, self.state.__repr__(), self.type.__repr__()) 

# set up route functions
## Main route
@app.route('/')
def index():
    parks = session.query(Park).all()
    num_parks = len(parks)
    return render_template('index.html', num_parks=num_parks)

@app.route('/stateForm')
def stateForm():
    states = session.query(State).all()
    return render_template('stateForm.html', states=states)


@app.route('/stateResult',methods=["GET"])
def stateResult():
    if request.method == "GET":
        # print(request.args) 
        state_name = request.args.get("state")
        state = session.query(State).filter_by(name=state_name).first()
        if not state:
            return "Not such state! "

        types = {}
        for park in state.parks:
            types[park.type.name] = types.get(park.type.name, 0) + 1

        save_figure(types, state_name)

        #construct x label and y label
        type_names = {}
        i = 1
        for t in types:
            tag = "#" + str(i)
            type_names[tag] = t
            i += 1
        return render_template('stateResult.html', types = type_names, state_name = state_name)
    return "Nothing was selected this time!"


@app.route('/park/<park_name>')
def park(park_name):
    park = session.query(Park).filter_by(name=park_name).first()
    if park:
        info = ParkInfo(park).get_info()
    else:
        info = None
    return render_template('parkInfo.html', info = info)



@app.route('/stateTypeResult/<state_name>/<type_name>', methods=["GET"])
def stateTypeResult(state_name, type_name):
    state = session.query(State).filter_by(name = state_name).first()
    type = session.query(Type).filter_by(name = type_name).first()

    parks = session.query(Park).filter_by(state=state, type = type).all()
    return render_template('stateTypeResult.html', parks = parks)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
 
if __name__ == '__main__':
    db.create_all() 
    web_scraping()
    main_populate("park_data.csv") 
    app.run(use_reloader=False) 





