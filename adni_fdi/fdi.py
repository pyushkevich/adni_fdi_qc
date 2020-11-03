from flask import Flask, render_template, send_file, Blueprint
from . import google_auth
import os

bp = Blueprint('fdi', __name__)



@bp.route('/')
def hello_world():
    return 'Hello World!'


@bp.route('/api/mesh/<id>/<method>/mesh.vtk', methods=('GET',))
def load_mesh(id, method):
    root_path='/Users/pauly/studies/adni_deface/qc_setup/test/surf'
    file = os.path.join(root_path, '%s/%s_%s_surface.vtk' % (id, id, method))
    return send_file(file)


@bp.route('/viewer/<id>/<method>')
def test_viewer(id, method):
    user_info=None
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
    return render_template('viewer.html', id=id, method=method, user=user_info)
