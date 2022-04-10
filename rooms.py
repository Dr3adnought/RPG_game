# A dictionary linking a room to other rooms
rooms = {

    'Great Hall': {                                                 # main feature interior of castl black, center of structure
        'deets': 'this is a great feasting hall, exits lie to the north, eastnorth, eastsouth, south and west.',
        'north': 'Kitchen',
        'eastnorth': 'The Shieldhall',
        'eastsouth': 'East Courtyard',
        'west': 'West Courtyard',
        'south': 'Twenyard',
        'item': 'key',
    },
    'Kitchen': {                                                    # where food is prepped, E of pantry, N of great hall
        'deets': 'this is a kitchen, exits lie to the west, south and east. The are stairs ascending upwards as well.',
        'west': 'Pantry',
        'south': 'Great Hall',
        'east': 'The Shieldhall',
        'upstairs': 'Cook\'s Quarters',
        'item': 'pan',
    },
    'Pantry': {                                                     # where food is stored, W of kitchen, above W Vaults
        'deets': 'this is a pantry, exits lie to the east and south. You can also see stairs descending down.',
        'downstairs': 'The Vaults West',
        'east': 'Kitchen',
        'south': 'West Courtyard',
        'item': 'bread',
    },
    'The Vaults West': {                                            # W room of underground vault
        'deets': 'this is an underground cellar of sorts, exits lie to the east and the ascending stairs from whence you came.',
        'upstairs': 'Pantry',
        'east': 'The Vaults East',
        'item': 'frozen meat',
    },
    'The Vaults East': {                                            # E room of underground vault, under kitchen
        'deets': 'this is an extension of the same underground cellar, exits lie to the east and west.',
        'west': 'The Vaults West',
        'east': 'The Library West',
        'item': 'frozen meat',
    },
    'The Library West': {                                           # W room of underground library, under shieldhall
        'deets': 'this is an underground library, exits lie to the east and west.',
        'west': 'The Vaults East',
        'east': 'The Library East',
        'item': 'books',
    },
    'The Library East': {                                           # E room of underground library, under armory
        'deets': 'this is an extension of the underground library, exits lie to the west and ascending stairs.',
        'west': 'The Library West',
        'upstairs': 'Armory',
        'item': 'scrolls',
    },
    'The Shieldhall': {                                             # where great feast are taken, adjoined by both kitchen and great hall
        'deets': 'this is the primary feasting hall, exits lie to the westnorth, westsouth, south and east.',
        'westnorth': 'Kitchen',
        'westsouth': 'Great Hall',
        'south': 'East Courtyard',
        'east': 'East Courtyard',
        'item': 'ale',
    },
    'East Courtyard': {                                             # large courtyard on E side of great hall
        'deets': 'this is the eastern courtyard, you see the Shieldhall to the north, another entrance to the Shieldhall to the westnorth, the Great Hall to the westsouth, the South East Centre Watch Tower to the south and the Training Yard to the east. Beyond that, the accoutrements of the eastern wall',
        'north': 'The Shieldhall',
        'westnorth': 'The Shieldhall',
        'westsouth': 'Great Hall',
        'east': 'Training Yard',
        'south': 'South East Centre Watch Tower',
    },
    'Training Yard': {                                              # larger training yard on E side of dining hall
        'deets': 'this is the Training Yard, the East Courtyard lies directly to the west. To the northeast is the imposing Great Door to the Tunnel Under the Wall.  To the northwest is the Armory. To the south lies the South East Middle Watch Tower. Entrances to the Eastgate South lie to the eastsouth, and Eastgate North to the eastnorth, respectively.',
        'west': 'East Courtyard',
        'northeast': 'Great Door to the Tunnel Under the Wall',
        'northwest': 'Armory',
        'south': 'South East Middle Watch Tower',
        'eastsouth': 'Eastgate South',
        'eastnorth': 'Eastgate North',
        'east': 'Eastgate',
    },
    'West Courtyard': {                                             # western courtyard and small training yard
        'northeast': 'Pantry',
        'north': 'Elevator to the Top of the Wall',
        'northwest': 'Flint Barracks',
        'west': 'Westgate',
        'westnorth': 'The Tower of the Guards',
        'westsouth': 'The King\'s Tower',
        'upstairs': 'West Overgate',
    },
    'Flint Barracks': {                                             # 2nd floor Barracks E of TotG, residence most of brothers of the night's watch reside
        'upstairs': 'Flint Barracks Second Floor',
        'downstairs': 'The Vaults West',
        'south': 'West Courtyard',
        'east': 'Tower of the Guards',
    },
    'Flint Barracks Second Floor': {                                # 2nd floor Barracks E of TotG, residence most of BotNW reside
        'downstairs': 'Flint Barracks',
        'west': 'Tower of the Guards Second Floor',
    },
    'Tower of the Guards': {                                        # ground floor of TotG, large structure that makes up remainder of West wall
        'upstairs': 'Tower of the Guards Second Floor',
        'south': 'North Westgate',
    },
    'Tower of the Guards Second Floor': {                           # 2nd floor of TotG, large structure that makes up remainder of West wall
        'upstairs': 'Tower of the Guards Third Floor',
        'downstairs': 'Tower of the Guards',
        'south': 'North Westgate Second Floor',
        'east': 'Tower of the Guards Second Floor'
    },
    'Tower of the Guards Third Floor': {                            # 3rd floor of TotG, large structure that makes up remainder of West wall
        'upstairs': 'Tower of the Guards Fourth Floor',
        'downstairs': 'Tower of the Guards Second Floor',
        'south': 'West Overgate',
    },
    'Tower of the Guards Fourth Floor': {                           # top floor of TotG, large structure that makes up remainder of West wall
        'downstairs': 'Tower of the Guards Third Floor',
    },
    'North Westgate': {                                             # ground floor of defensive structure at north end of gate
        'north': 'Tower of the Guards',
        'upstairs': 'North Westgate Second Floor',
    },
    'North Westgate Second Floor': {                                # 2nd floor of defensive structure at north end of gate
        'north': 'Tower of the Guards Second Floor',
        'upstairs': 'West Overgate',
        'downstairs': 'North Westgate',
    },
    'West Overgate': {                                               # walkway over gate (3rd level above ground)
        'east': 'Overlook to the West Courtyard',
        'west': 'Overlook to the King\'s Road',
        'north': 'Tower of the Guards Third Floor',
        'south': 'King\'s Tower Third Floor',
        'downstairs south end': 'South Westgate Second Floor',
        'downstairs north end': 'North Westgate Second Floor',
    },
    'South Westgate': {                                             # ground floor of defensive structure at south end of gate
        'south': 'King\'s Tower',
        'upstairs': 'South Westgate Second Floor',
    },
    'South Westgate Second Floor': {                                # 2nd floor of defensive structure at south end of gate
        'south': 'King\'s Tower Second Floor',
        'upstairs': 'West Overgate',
        'downstairs': 'South Westgate',
    },
    'King\'s Tower': {                                              # ground floor of King's Tower
        'north': 'South Westgate',
        'upstairs': 'King\'s Tower Second Floor',
    },
    'King\'s Tower Second Floor': {                                 # 2nd floor of King's Tower
        'north': 'South Westgate Second Floor',
        'upstairs': 'King\'s Tower Third Floor',
        'downstairs': 'King\'s Tower',
        'east': 'King\'s Tower Lower Battlement',
    },
    'King\'s Tower Third Floor': {                                  # 3rd floor of King's Tower
        'north': 'West Overgate',
        'upstairs': 'King\'s Tower Fourth Floor',
        'downstairs': 'King\'s Tower Second Floor',
        'east': 'King\'s Tower Upper Battlement',
    },
    'King\'s Tower Fourth Floor': {                                 # 4th floor of King's Tower
        'upstairs': 'King\'s Tower Fifth Floor',
        'downstairs': 'King\'s Tower Third Floor',
    },
    'King\'s Tower Fifth Floor': {                                  # 5th floor of King's Tower
        'upstairs': 'King\'s Tower Perch',
        'downstairs': 'King\'s Tower Fourth Floor',
    },
    'King\'s Tower Perch': {                                        # top floor of King's Tower
        'downstairs': 'King\'s Tower Fifth Floor',
    },
    'King\'s Tower Lower Battlement': {                             # lower b'ment between King's Tower and LC's side stoop
        'upstairs': 'King\'s Tower Upper Battlement',
        'east': 'Lord Commander\'s Stoop',
        'west': 'King\'s Tower Second Floor',
    },
    'King\'s Tower Upper Battlement': {                             # upper b'ment between King's Tower and LC's roof b'ment
        'downstairs': 'King\'s Tower Lower Battlement',
        'east': 'Lord Commander\'s Battlement',
        'west': 'King\'s Tower Third Floor',
    },
    'Lord Commander\'s Side Stoop': {                               # LC's wooden deck west side of quarters, 1 level off ground
        'north': 'Lord Commander\'s Front Stoop',
        'east': 'Lord Commander\'s Quarters',
        'west': 'King\'s Tower Lower Battlement',
        'downstairs': 'West Courtyard',
    },
    'Lord Commander\'s Front Stoop': {                               # LC's wooden deck north of quarters, 1 level off ground
        'south': 'Lord Commander\'s Quarters',
        'west': 'Lord Commander\'s Side Stoop',
        'downstairs': 'West Courtyard',
    },
    'Lord Commander\'s Quarters': {                                 # LC's quarters W of The Rookery tower
        'upstairs': 'Lord Commander\'s Battlement',
        'downstairs': 'Lord Commander\'s Stewards Quarters',
        'west': 'Lord Commander\'s Side Stoop',
        'north': 'Lord Commander\'s Front Stoop',
    },
    'Lord Commander\'s Stewards Quarters': {                        # LC's stewards quarters below LC's quarters
        'upstairs': 'Lord Commander\'s Quarters',
    },
    'Lord Commander\'s Battlement': {                               # roof battlement above LC's quarters
        'downstairs': 'Lord Commander\'s Quarters',
        'west': 'King\'s Tower Upper Battlement',
        'east': 'The Rookery Scroll Room',
    },
    'The Rookery Scroll Room': {                                    # 3rd floor of tower on center of southern wall
        'upstairs': 'Maester\'s Quarters',
        'downstairs': 'The Rookery Second Floor',
        'west': 'Lord Commander\'s Battlement',
        'east': 'Rookery Upper Battlement',
    },
    'Maester\'s Quarters': {                                        # 4th floor of tower on center of southern wall
        'upstairs': 'Maester\'s Raven Loft',
        'downstairs': 'The Rookery Scroll Room',
    },
    'Maester\'s Raven Loft': {                                      # top (5th) floor of tower on center of southern wall
        'downstairs': 'Maester\'s Quarters',
        'north': 'Rookery Raven Loft North Balcony',
        'south': 'Rookery Raven Loft South Balcony',
        'east': 'Rookery Raven Loft East Balcony',
        'west': 'Rookery Raven Loft West Balcony',
    },
    'The Rookery Second Floor': {                                   # 2nd floor of tower on center of southern wall
        'upstairs': 'The Rookery Scroll Room',
        'downstairs': 'The Rookery',
        'west': 'Lord Commander\'s Front Stoop',
        'east': 'Rookery Lower Battlement',
        'north': 'Courtyard Overwalk',
    },
    'The Rookery': {                                                # 1st floor of tower on center of southern wall
        'upstairs': 'The Rookery Second Floor',
        'downstairs': 'The Rookery Basement',
        'north': 'Twenyard',
    },
    'Twenyard': {                                                   # area between the west and east courtyards
        'north': 'Great Hall',
        'west': 'West Courtyard',
        'east': 'East Courtyard',
        'south': 'The Rookery',
    },
    'Rookery Lower Battlement': {                                   # Lower battlement between The Rookery and watch tower to E
        'west': 'The Rookery Second Floor',
        'east': 'South East Centre Watch Tower Second Floor',
    },
    'Rookery Upper Battlement': {                                   # Upper battlement between The Rookery and watch tower to E
        'west': 'The Rookery Scroll Room',
        'east': 'South East Centre Watch Tower Top Floor',
    },
    'South East Centre Watch Tower': {                              # 1st floor of watch tower immediately E of The Rookery
        'upstairs': 'South East Centre Watch Tower Second Floor',
    },
    'South East Centre Watch Tower Second Floor': {                 # 2nd floor of watch tower immediately E of The Rookery
        'upstairs': 'South East Centre Watch Tower Top Floor',
        'downstairs': 'South East Centre Watch Tower',
        'west': 'Rookery Lower Battlement',
        'east': 'South East Centre Lower Battlement',
    },
    'South East Centre Watch Tower Top Floor': {                    # top floor of watch tower immediately E of The Rookery (46)
        'downstairs': 'South East Centre Watch Tower Second Floor',
        'west': 'Rookery Upper Battlement',
        'east': 'South East Centre Upper Battlement',
    },
    'South East Centre Lower Battlement': {                         # lower b'ment between Centre & Middle watch towers on S wall
        'west': 'South East Centre Watch Tower Second Floor',
        'east': 'South East Middle Watch Tower Second Floor',
    },
    'South East Centre Upper Battlement': {                         # upper b'ment between Centre & Middle watch towers on S wall
        'west': 'South East Centre Watch Tower Top Floor',
        'east': 'South East Middle Watch Tower Top Floor',
    },
    'South East Middle Watch Tower': {                              # ground floor of watch tower immediately W of The Lance
        'upstairs': 'South East Middle Watch Tower Second Floor',
    },
    'South East Middle Watch Tower Second Floor': {                 # 2nd floor of watch tower immediately W of The Lance (50)
        'upstairs': 'South East Middle Watch Tower Top Floor',
        'downstairs': 'South East Middle Watch Tower',
        'west': 'South East Centre Lower Battlement',
        'east': 'West Lance Lower Battlement',
    },
    'South East Middle Watch Tower Top Floor': {                    # 3rd floor of watch tower immediately W of The Lance
        'downstairs': 'South East Middle Watch Tower Second Floor',
        'west': 'South East Centre Upper Battlement',
        'east': 'West Lance Upper Battlement',
    },
    'West Lance Lower Battlement': {                                # lower level of b'ment connecting The Lance to SE Middle watch tower
        'west': 'South East Middle Watch Tower Second Floor',
        'east': 'The Lance Second Floor',
    },
    'West Lance Upper Battlement': {                                # upper level of b'ment connecting The Lance to SE Middle watch tower
        'west': 'South East Middle Watch Tower Top Floor',
        'east': 'The Lance Third Floor',
    },
    'The Lance': {                                                  # ground floor SE most tower, SE corner of Castle Black
        'upstairs': 'The Lance Second Floor',
        'north': 'Training Yard',
        'west': 'East Courtyard',
    },
    'The Lance Second Floor': {                                     # 2nd floor SE most tower, SE corner of Castle Black
        'downstairs': 'The Lance',
        'upstairs': 'The Lance Third Floor',
        'north': 'Eastgate South Lower Battlement',
        'west': 'West Lance Lower Battlement',
    },
    'The Lance Third Floor': {                                      # 3rd floor SE most tower, SE corner of Castle Black
        'downstairs': 'The Lance Second Floor',
        'upstairs': 'The Lance Fourth Floor',
        'north': 'Eastgate South Upper Battlement',
        'west': 'West Lance Upper Battlement',
    },
    'The Lance Fourth Floor': {                                     # Top floor SE most tower, SE corner of Castle Black
        'downstairs': 'The Lance Third Floor',
    },
    'Eastgate South Lower Battlement': {                            # Lower b'ment connecting Eastgate watch tower to The Lance
        'north': 'Eastgate South Second Floor',
        'south': 'The Lance Second Floor',
    },
    'Eastgate South Upper Battlement': {                            # Lower b'ment connecting Eastgate watch tower to The Lance
        'north': 'Eastgate South Third Floor',
        'south': 'The Lance Third Floor',
    },
    'Eastgate South': {                                             # 60
        'upstairs': 'Eastgate South Second Floor',
        'west': 'Training Yard',
    },
    'Eastgate South Second Floor': {
        'south': 'Eastgate South Lower Battlement',
        'upstairs': 'Eastgate South Third Floor',
        'downstairs': 'Eastgate South',
    },
    'Eastgate South Third Floor': {
        'south': 'Eastgate South Upper Battlement',
        'downstairs': 'Eastgate South Second Floor',
        'north': 'Eastgate Overlook',
    },
    'Eastgate Overlook': {
        'east': 'Overlook of King\'s Road East',
        'west': 'Overlook of Training Yard',
        'north': 'Eastgate North Third Floor',
        'south': 'Eastgate South Third Floor',
    },
    'Eastgate North Third Floor': {
        'north': 'Eastgate North Upper Battlement',
        'upstairs': 'Eastgate Overlook',
        'downstairs': 'Eastgate North',
    },
    'Eastgate North Second Floor': {
        'north': 'Eastgate North Lower Battlement',
        'upstairs': 'Eastgate North Third Floor',
        'downstairs': 'Eastgate North',
    },
    'Eastgate North': {
        'west': 'Training Yard',
        'upstairs': 'Eastgate North Second Floor',
    },
    'Eastgate North Lower Battlement': {
        'north': 'Hardin\'s Tower Second Floor',
        'south': 'Eastgate North Second Floor',
    },
    'Eastgate North Upper Battlement': {
        'north': 'Hardin\'s Tower Third Floor',
        'south': 'Eastgate North Third Floor',
    },
    'Hardin\'s Tower': {
        'west': 'Training Yard',
        'upstairs': 'Hardin\'s Tower Second Floor',
    },
    'Hardin\'s Tower Second Floor': {                               # 70
        'downstairs': 'Hardin\'s Tower',
        'upstairs': 'Hardin\'s Tower Third Floor',
        'south': 'Eastgate North Lower Battlement',
    },
    'Hardin\'s Tower Third Floor': {
        'downstairs': 'Hardin\'s Tower Second Floor',
        'upstairs': 'Hardin\'s Tower Fourth Floor',
        'south': 'Eastgate North Upper Battlement',
    },
    'Hardin\'s Tower Fourth Floor': {
        'downstairs': 'Hardin\'s Tower Third Floor',
    },
    'Armory': {
        'east': 'Training Yard',
        'south': 'East Courtyard',
        'downstairs': 'The Library East',
    },
    'Westgate': {
        'east': 'West Courtyard',
    },
    'Eastgate': {                                                   # 75
        'west': 'Training Yard',
    },
    'Cook\'s Quarters': {
        'deets': 'this is the Cook\'s Quarters, the only possible exit is the descending staircase to the Kitchen.',
        'downstairs': 'Kitchen',
    },
    'Rookery Raven Loft North Balcony': {                           #
        'south': 'Maester\'s Raven Loft',
    },
    'Rookery Raven Loft South Balcony': {                           #
        'north': 'Maester\'s Raven Loft',
    },
    'Rookery Raven Loft East Balcony': {                            #
        'west': 'Maester\'s Raven Loft',
    },
    'Rookery Raven Loft West Balcony': {                            # 80
        'east': 'Maester\'s Raven Loft',
    },
}
