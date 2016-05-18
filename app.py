from flask import Flask, render_template, request 
from operator import itemgetter
import csv
SCORE_FNAME = './static/data/scorecard_elements.csv'


app = Flask(__name__)


def get_data():
     with open(SCORE_FNAME, encoding='latin1') as f:
        newrows = []
        for row in csv.DictReader(f):
            if row['GRAD_DEBT_MDN_SUPP'] != 'PrivacySuppressed' and row['GRAD_DEBT_MDN_SUPP'] != 'NULL':
                row['GRAD_DEBT_MDN_SUPP'] = float(row['GRAD_DEBT_MDN_SUPP'])
                newrows.append(row)
        return newrows

def filter_data(STABBR='', sortby=None):
    upstate = STABBR.upper()
    rows = [d for d in get_data() if upstate in d['STABBR']]
    if sortby == 'Highest Debt':
        return sorted(rows, key=itemgetter('GRAD_DEBT_MDN_SUPP'), reverse=True)
    elif sortby == 'Lowest Debt':
        return sorted(rows, key=itemgetter('GRAD_DEBT_MDN_SUPP'))
    else:
        return sorted(rows, key=itemgetter('STABBR'))

@app.route("/")
def homepage():
    html = render_template('index.html')
    return html

@app.route("/results")
def results():
    _sortby =  request.args.get('sortby')
    _STABBR =  request.args.get('STABBR')
    schools = filter_data(STABBR=_STABBR, sortby=_sortby)
    html = render_template('results.html', STABBR=_STABBR,
                           scorecard_elements=schools, sortby=_sortby)
    return html


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)