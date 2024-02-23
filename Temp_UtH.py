head = {
    'Value':7,
    'Next':{
        'Value':4,
        'Next':{
            'Value':3,
            'Next':{
                'Value':2,
                'Next':{
                    'Value':1,
                    'Next':None
                }
            }
        }
    }
}

print(head['Next']['Next']['Next']['Value'])