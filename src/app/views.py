from flask import Response

from . import app 

@app.route('/healthcheck')
def healthcheck():
    return 'OK'

@app.errorhandler(404)
def page_not_found(e):
    return Response(str(e), status=404)

@app.errorhandler(Exception)
def unexpected_error(e):
    logging.exception('Unexpected error')
    return Response('Unexpected error', status=500)
