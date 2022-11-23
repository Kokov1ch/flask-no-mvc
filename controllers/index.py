from app import app
import constants
from flask import render_template
@app.route('/', methods=['GET'])
def index():
 # выводим форму
    html = render_template(
     'index.html',
     program_list=constants.programs,
     subject_list=constants.subjects,
     olympiad_list=constants.olympiad,
     len=len
    )

    return html
