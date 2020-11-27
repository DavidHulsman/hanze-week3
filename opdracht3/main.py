from flask import render_template, request
from datetime import datetime
from models import app, db, Meting


@app.route('/')
def index():
    """Toon de metingen op een kaart"""
    return render_template('index.html', metingen=Meting.query.all())

@app.route('/table')
def table():
    """Toon de metingen in een tabel"""
    return render_template('table.html', metingen=Meting.query.all())

@app.route('/m')
def bewaar_nieuwe_meting():
    uuid = request.args.get('uuid', default=None, type=str)
    lat = request.args.get('lat', default=None, type=float)
    lng = request.args.get('lng', default=None, type=float)
    if None in [uuid, lat, lng]:
        return 'Gebruik: /m?uuid=[WAARDE]&lat=[WAARDE]&lng=[WAARDE]'

    nieuwe_meting = Meting(uuid=uuid, lat=lat, lng=lng, tijdstempel=datetime.now())
    db.session.add(nieuwe_meting)
    db.session.commit()
    return f'<small>({str(nieuwe_meting.uuid)},{str(nieuwe_meting.lat)},{str(nieuwe_meting.lng)},{str(nieuwe_meting.tijdstempel)})</small>'
