from flask import Flask

app = Flask(__name__)

from backend import routes  # import routes to register them
