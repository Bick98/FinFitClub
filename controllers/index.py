from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index_model import get_client, get_new_client, get_trainer_for_client,zapis_na_trenirovku, pay_tr


@app.route('/', methods=['get'])
def index():
    conn = get_db_connection()

    if request.values.get('client'):
        idClients = int(request.values.get('client'))
        session['idClients'] = idClients
    elif request.values.get('new_fio'):
        new_fio = request.values.get('new_fio')
        new_age = request.values.get('new_age')
        new_gender = request.values.get('new_gender')
        new_pass = request.values.get('new_pass')
        session['reader_id'] = get_new_client(conn, new_fio, new_age, new_gender, new_pass)
    elif request.values.get('return'):
        idPoseshenie = int(request.values.get('return'))
        pay_tr(conn, idPoseshenie)
    elif request.values.get('training'):
        idPoseshenie = int(request.values.get('training'))
        zapis_na_trenirovku(conn, session['idClients'], idPoseshenie)
    elif request.values.get('noselect'):
        a=1
    else:
        session['idClients'] = 1


    df_client = get_client(conn)
    df_poseshenie = get_trainer_for_client(conn, session['idClients'])

    # выводим форму
    html = render_template(
        'index.html',
        idClients=session['idClients'],
        combo_box=df_client,
        poseshenie=df_poseshenie,
        len=len
    )
    return html
