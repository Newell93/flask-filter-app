from operator import itemgetter
import csv
SCORE_FNAME = './static/data/scorecard_elements.csv'
def get_data():
    with open(SCORE_FNAME) as f:
    	newrows = []
        for row in csv.DictReader(f):
        	if row['STABBR'] == 'AL':
        		newrows.append(row)
        return newrows
