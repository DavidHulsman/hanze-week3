from flask import render_template, request
from datetime import datetime
from models import app, db, Meting, Test


@app.route('/')
def index():
    """Toon de metingen"""
    return render_template('index.html', metingen=Meting.query.all())


@app.route('/m')
def bewaar_nieuwe_meting():
    meting = request.args.get('meting', default=None, type=float)
    if meting is None:
        return 'Gebruik: <b>/m?meting=</b>waarde'

    nieuwe_meting = Meting(meetwaarde=meting, tijdstempel=datetime.now())
    db.session.add(nieuwe_meting)
    db.session.commit()
    return f'<small>({str(nieuwe_meting.meetwaarde)},{str(nieuwe_meting.tijdstempel)})</small>'
