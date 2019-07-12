activate_this = '/path/to/your/project/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/path/to/your/project/")

from app import flask_app as application
application.secret_key = 'Add your secret key'