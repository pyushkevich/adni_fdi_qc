from flask import Flask, render_template, send_file
import functools
import json
import os

from authlib.integrations.requests_client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth

app = Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)
app.register_blueprint(google_auth.app)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/mesh/<id>/<method>/mesh.vtk', methods=('GET',))
def load_mesh(id, method):
    root_path='/Users/pauly/studies/adni_deface/qc_setup/test/surf'
    file = os.path.join(root_path, '%s/%s_%s_surface.vtk' % (id, id, method))
    return send_file(file)


@app.route('/viewer/<id>/<method>')
def test_viewer(id, method):
    user_info=None
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
    return render_template('viewer.html', id=id, method=method, user=user_info)


if __name__ == '__main__':
    app.run()
