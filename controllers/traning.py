import static.desc
from app import app
from flask import render_template, request,session
from utils import get_db_connection
from models.traning_model import get_spec

# @app.route('/traning', methods=['get', 'post'])
# def traning():
#     conn = get_db_connection()
#     df_spec = get_spec(conn)
#
#     selected = ['ОФП', 'Бодибилдинг']
#
#     if request.values.get('select'):
#         choice = request.values.get('select')
#     else:
#         choice = ''
#
#     if choice == 'ОФП':
#         f = 2
#         df_desc_dict = static.desc.spec_dict[1]
#         df_name_dict = 'ОФП'
#     elif choice == 'Бодибилдинг':
#         f = 2
#         df_desc_dict = static.desc.spec_dict[2]
#         df_name_dict = 'Бодибилдинг'
#     elif request.form.get('clear'):
#         f = 1
#         df_desc_dict = {}
#         df_name_dict = ''
#     else:
#         f = 1
#         df_desc_dict = {}
#         df_name_dict = ''
#         session['idTrainerSpec'] = 1
#
#
#
#     html = render_template(
#         'traning.html',
#         discription = df_desc_dict,
#         combo_box=df_spec,
#         idClients = session['idTrainerSpec'],
#         name = df_name_dict,
#         selected=selected,
#         flag = f,
#         len=len
#
#
#     )
#     return html

@app.route('/traning', methods=['get', 'post'])
def traning():
    conn = get_db_connection()
    df_spec = get_spec(conn)



    if request.values.get('spec'):
        f = 2
        idTrainerSpec = int(request.values.get('spec'))
        image = '/static/images/'+str(idTrainerSpec)+'.jpg'
        df_desc_dict = static.desc.spec_dict[idTrainerSpec]
        session['idTrainerSpec'] = idTrainerSpec
    elif request.form.get('clear'):
        f = 1
        df_desc_dict = {}
        session['idTrainerSpec'] = 1
        image = None
    else:
        f = 1
        df_desc_dict = {}
        session['idTrainerSpec'] = 1
        image = None



    html = render_template(
        'traning.html',
        discription = df_desc_dict,
        combo_box=df_spec,
        image= image,
        idTrainerSpec = session['idTrainerSpec'],
        flag = f,
        len=len


    )
    return html