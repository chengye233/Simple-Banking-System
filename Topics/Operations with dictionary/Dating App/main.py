def select_dates(potential_dates):
    names = [d.get('name') for d in potential_dates if
             'art' in d.get('hobbies') and d.get('age') > 30 and d.get('city') == 'Berlin']
    return ', '.join(names)
