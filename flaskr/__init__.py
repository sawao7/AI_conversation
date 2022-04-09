from flask import Flask, render_template

app = Flask(__name__)

import flaskr.views
import flaskr.sqlite
import flaskr.openai
