from helpers import get_data
data = get_data()
def print_record_count():
    print(len(data))

def filter_data(STABBR='', sortby=None):
    upname = STABBR.upper()
    rows = [g for g in get_data() if upname in g['STABBR']]
    if sortby == 'High_Debt_Schools':
        return sorted(rows, key=itemgetter('GRAD_DEBT_MDN_SUPP'), reverse=True)
    elif sortby == 'Low_Debt_Schools':
        return sorted(rows, key=itemgetter('GRAD_DEBT_MDN_SUPP'))
    else:
        return sorted(rows, key=itemgetter('STABBR'))
        return dogs
        

