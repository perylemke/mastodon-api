import pymongo
from decouple import config


engine = config('DB_URI', default='localhost', cast=str)
client = pymongo.MongoClient(engine)
db = client.mastodondb


members_list = [
    {
        '_id': 1,
        'name': "Brent Hinds",
        'birth_date': "1974/01/16",
        'instruments': [
            "Lead Guitar",
            "Backing Vocals",
            "Lead Vocals"
        ],
        'first_year': "2000",
        'last_year': "Present",
        'discography': [
            "Remission",
            "Leviathan",
            "Blood Mountain",
            "Crack the Skye",
            "The Hunter",
            "Once More 'Round the Sun",
            "Emperor of Sand",
            "Cold Dark Place",
            "Hushed and Grim"
        ]
    },
    {
        '_id': 2,
        'name': "Bill Kelliher",
        'birth_date': "1971/03/23",
        'instruments': [
            "Rhythm Guitar",
            "Backing Vocals"
        ],
        'first_year': "2000",
        'last_year': "Present",
        'discography': [
            "Remission",
            "Leviathan",
            "Blood Mountain",
            "Crack the Skye",
            "The Hunter",
            "Once More 'Round the Sun",
            "Emperor of Sand",
            "Cold Dark Place",
            "Hushed and Grim"
        ]
    },
    {
        '_id': 3,
        'name': "Troy Sanders",
        'birth_date': "1973/09/08",
        'instruments': [
            "Bass",
            "Keyboards",
            "Backing Vocals",
            "Lead Vocals"
        ],
        'first_year': "2000",
        'last_year': "Present",
        'discography': [
            "Remission",
            "Leviathan",
            "Blood Mountain",
            "Crack the Skye",
            "The Hunter",
            "Once More 'Round the Sun",
            "Emperor of Sand",
            "Cold Dark Place",
            "Hushed and Grim"
        ]
    },
    {
        '_id': 4,
        'name': "Brann Dailor",
        'birth_date': "1975/03/19",
        'instruments': [
            "Drums",
            "Percussion",
            "Backing Vocals",
            "Lead Vocals"
        ],
        'first_year': "2000",
        'last_year': "Present",
        'discography': [
            "Remission",
            "Leviathan",
            "Blood Mountain",
            "Crack the Skye",
            "The Hunter",
            "Once More 'Round the Sun",
            "Emperor of Sand",
            "Cold Dark Place",
            "Hushed and Grim"
        ]
    },
    {
        '_id': 5,
        'name': "Eric Saner",
        'birth_date': "",
        'instruments': [
            "Lead Vocals"
        ],
        'first_year': "2000",
        'last_year': "2001",
        'discography': [
            ""
        ]
    }
]

members_data = db.members.insert_many(members_list)
print(members_data.inserted_ids)
