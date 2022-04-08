# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'Great Hall': {
        'north': 'Kitchen',
        'eastnorth': 'The Shieldhall',
        'eastsouth': 'East Courtyard',
        'west': 'West Courtyard',
        'south': 'The Rookery Tower',
        'item': 'key'
    },
    'Kitchen': {
        'west': 'Pantry',
        'south': 'Great Hall',
        'east': 'The Shieldhall',
        'upstairs': 'Cook\'s Quarters',
        'item': 'pan',
    },
    'Pantry': {
        'downstairs': 'The Vaults',
        'east': 'Kitchen',
        'south': 'West Courtyard',
        'item': 'bread',
    },
    'The Vaults West': {
        'upstairs': 'Pantry',
        'east': 'The Vaults East',
        'item': 'frozen meat'
    },
    'The Vaults East': {
        'west': 'The Vaults West',
        'east': 'The Library',
        'item': 'frozen meat',
    },
    'The Library West': {
        'west': 'The Vaults East',
        'east': 'The Library East',
        'item': 'books',
    },
    'The Library West': {
        'west': 'The Library West',
        'upstairs': 'XXX------XXX',
        'item': 'scrolls',
    },
    'The Shieldhall': {
        'westnorth': 'Kitchen',
        'westsouth': 'Great Hall',
        'south': 'East Courtyard',
        'east': 'East Courtyard',
        'item': 'ale',
    },
    'East Courtyard': {
        'north': 'The Shieldhall',
        'westnorth': 'The Shieldhall',
        'westsouth': 'Great Hall',
        'east': 'Training Yard',
        'south': 'South East Centre Watchtower'
    },
    'Training Yard': {
        'west': 'East Courtyard',
        'northeast': 'Great Door to the Tunnel Under the Wall',
        'northwest': 'Lord Commander\'s Quarters',
        'south': 'South East Middle Watch Tower',
        'east': 'East South Watch Tower',
    },
    'West Courtyard': {
        'northeast': 'Pantry',
        'north': 'Elevator to the Top of the Wall',
        'northwest': 'Flint Barracks',
        'west': 'The Gate',
        'westnorth': 'The Tower of the Guards',
        'westsouth': 'The King\'s Tower',
        'upstairs': 'The Overgate',
    },
    'Flint Barracks': {
        'upstairs': 'Flint Barracks Second Floor',
        'downstairs': 'The Vaults West',
        'south': 'West Courtyard',
        'east': 'Tower of the Guards',
    },
    'Flint Barracks Second Floor': {
        'downstairs': 'Flint Barracks',
        'east': 'Tower of the Guards Second Floor',
    },
    'Tower of the Guards': {
        'upstairs': 'Tower of the Guards Second Floor',
        'south': 'Northgate',
    },
    'Tower of the Guards Second Floor': {
        'upstairs': 'Tower of the Guards Third Floor',
        'downstairs': 'Tower of the Guards',
        'south': 'Northgate Second Floor',
    },
    'Tower of the Guards Third Floor': {
        'upstairs': 'Tower of the Guards Fourth Floor',
        'downstairs': 'Tower of the Guards Second Floor',
        'south': 'The Overgate',
    },
    'Tower of the Guards Fourth Floor': {
        'downstairs': 'Tower of the Guards Third Floor',
    },
    'Northgate': {
        'north': 'Tower of the Guards',
        'upstairs': 'Northgate Second Floor',
    },
    'Northgate Second Floor': {
        'north': 'Tower of the Guards Second Floor',
        'upstairs': 'The Overgate',
        'downstairs': 'Northgate',
    },
    'The Overgate': {
        'east': 'Overlook to the West Courtyard',
        'west': 'Overlook to the King\'s Road',
        'north': 'Tower of the Guards Third Floor',
        'south': 'King\'s Tower Third Floor',
    },
    'Southgate': {
        'south': 'King\'s Tower',
        'upstairs': 'Southgate Second Floor',
    },
    'Southgate Second Floor': {
        'south': 'King\'s Tower Second Floor',
        'upstairs': 'The Overgate',
        'downstairs': 'Southgate',
    },
    'King\'s Tower': {
        'north': 'Southgate',
        'upstairs': 'King\'s Tower Second Floor',
        'east': '',
    },
    'King\'s Tower Second Floor': {
        'north': 'Southgate Second Floor',
        'upstairs': 'King\'s Tower Third Floor',
        'downstairs': 'King\'s Tower',
        'east': '',
    },
    'King\'s Tower Third Floor': {
        'north': 'The Overgate',
        'upstairs': 'King\'s Tower Fourth Floor',
        'downstairs': 'King\'s Tower Second Floor',
        'east': '',
    },
    'King\'s Tower Fourth Floor': {
        'upstairs': 'King\'s Tower Fifth Floor',
        'downstairs': 'King\'s Tower Third Floor',
    },
    'King\'s Tower Fifth Floor': {
        'upstairs': 'King\'s Tower Perch',
        'downstairs': 'King\'s Tower Fourth Floor',
    },
    'King\'s Tower Perch': {
        'downstairs': 'King\'s Tower Fifth Floor',
    },
}
