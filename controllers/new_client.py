from app import app
from flask import render_template


@app.route('/new_client', methods=['get'])
def new_client():
    html = render_template(
        'new_client.html',
    )
    return html