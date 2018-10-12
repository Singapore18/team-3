

def initializeData(requests):
    requests.session['pending_resume'] = {
        "paul": {
            "name" : "paul",
            "interest" : ['singing', 'cooking'],
            "address" : 'Victoria Street 81',
            "work schedule" : "part-time"
        }
    }