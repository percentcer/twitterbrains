# Run a test server.
__author__ = 'spencer'

from app import app
app.run(host='0.0.0.0', port=8080, debug=True)
