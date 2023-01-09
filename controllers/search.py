from app import app
from flask import render_template, request
from utils import get_db_connection
from models.search_model import get_spec, get_trainers, card


@app.route('/search', methods=['get', 'post'])
def search():
    conn = get_db_connection()
    df_spec = get_spec(conn)
    df_trainers = get_trainers(conn)

    if request.form.get('clear'):
        spec = []
        trainers =[]
    else:
        spec = [int(item) for item in request.form.getlist('idTrainerSpec')]
        trainers = [int(item) for item in request.form.getlist('idTrainer')]

    df_card = card(conn, spec ,trainers)

    html = render_template(
        'search.html',
        spec=df_spec,
        trainers=df_trainers,
        card=df_card,
        sel_spec=spec,
        sel_trainers=trainers,
        len=len
    )
    return html