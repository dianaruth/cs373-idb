from unittest import main, TestCase
# from models import *
from flask import *
from sqlalchemy import *
from flask.ext.sqlalchemy import SQLAlchemy

class tests(TestCase):

    app = Flask(__name__)
    # use your own MySQL credentials
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jhlim84:jonghoonlim@localhost/swewarstest'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(app)

    if db is None :
        print("db is not connected")
    else :
        print("db is connected")

if __name__ == '__main__':
    main()
    
"""
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK

Name     Stmts   Miss  Cover
----------------------------
models      48      0   100%
tests       48      0   100%
----------------------------
TOTAL       96      0   100%
"""