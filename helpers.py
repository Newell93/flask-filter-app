from operator import itemgetter
import csv
SCORE_FNAME = './static/data/scorecard_elements.csv'
def get_data():
     with open(SCORE_FNAME, encoding='latin1') as f:
        newrows = []
        for row in csv.DictReader(f):
            if row['GRAD_DEBT_MDN_SUPP'] != 'PrivacySuppressed' and row['GRAD_DEBT_MDN_SUPP'] != 'NULL':
                row['GRAD_DEBT_MDN_SUPP'] = float(row['GRAD_DEBT_MDN_SUPP'])
                newrows.append(row)
        return newrows


