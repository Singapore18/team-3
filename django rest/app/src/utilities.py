

def initializeData(requests):
    requests.session['pending_resume'] = {
        "paul": {
            "name" : "paul",
            "interest" : ['singing', 'cooking'],
            "address" : 'Victoria Street 81',
            "work schedule" : "part-time"
        },
        "john": {
            "name" : "john",
            "interest" : ['dancing', 'running'],
            "address" : 'Ang Mo Kio Avenue 3',
            "work schedule" : "full time"
        },   
        "emily": {
            "name" : "emily",
            "interest" : ['dancing', 'singing'],
            "address" : '11 Toa Payoh Rise',
            "work schedule" : "full time"
        },  
        "amy": {
            "name" : "amy",
            "interest" : ['cooking', 'baking'],
            "address" : '79 Serangoon Road',
            "work schedule" : "part-time"
        },       
        "layla": {
            "name" : "layla",
            "interest" : ['eating', 'baking'],
            "address" : '79 Clementi Road',
            "work schedule" : "part-time"
        },           
    }
    requests.session['confirmed_resume'] = {
        "britney": {
            "name" : "britney",
            "interest" : ['cooking', 'gardening'],
            "address" : '9 Jurong East Road',
            "work schedule" : "part-time"
        },
        "roy": {
            "name" : "roy",
            "interest" : ['gardening'],
            "address" : '7 Ang Mo Kio',
            "work schedule" : "full time"
        },   
        "joe": {
            "name" : "joe",
            "interest" : ['dancing', 'singing'],
            "address" : '11 Toa Payoh Rise',
            "work schedule" : "full time"
        },  
        "don": {
            "name" : "don",
            "interest" : ['eating', 'sleeping'],
            "address" : '79 Serangoon Road',
            "work schedule" : "part-time"
        },       
        "jen": {
            "name" : "jen",
            "interest" : ['eating', 'baking'],
            "address" : '79 Clementi Road',
            "work schedule" : "part-time"
        },           
    }    