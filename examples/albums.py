import pymongo
from decouple import config


engine = config('DB_URI', default='localhost', cast=str)
client = pymongo.MongoClient(engine)
db = client.mastodondb


albums_list = [
    {
        '_id': 1,
        'name': "Remission",
        'release_date': "2002/05/28",
        'length': "50:22",
        'labels': [
            "Relapse"
        ],
        'members': [
            "Troy Sanders",
            "Brent Hinds",
            "Bill Kelliher",
            "Brann Dailor"
        ],
        'track_list': [
            "Crusher Destroyer",
            "March of the Fire Ants",
            "Where Strides the Behemoth",
            "Workhorse",
            "Ol'e Nessie",
            "Burning Man",
            "Trainwreck",
            "Trampled Under Hoof",
            "Trilobite",
            "Mother Puncher",
            "Elephant Man"
        ]
    },
    {
        '_id': 2,
        'name': "Leviathan",
        'release_date': "2004/08/31",
        'length': "46:43",
        'labels': [
            "Relapse"
        ],
        'members': [
            "Troy Sanders",
            "Brent Hinds",
            "Bill Kelliher",
            "Brann Dailor"
        ],
        'track_list': [
            "Blood and Thunder",
            "I Am Ahab",
            "Seabeast",
            "Island",
            "Iron Tusk",
            "Megalodon",
            "Naked Burn",
            "Aqua Dementia",
            "Hearts Alive",
            "Joseph Merrick"
        ]
    },
    {
        '_id': 3,
        'name': "Blood Mountain",
        'release_date': "",
        'length': "51:02",
        'labels': [
            "Reprise",
            "Relapse"
        ],
        'members': [
            "Troy Sanders",
            "Brent Hinds",
            "Bill Kelliher",
            "Brann Dailor"
        ],
        'track_list': [
            "The Wolf Is Loose",
            "Crystal Skull",
            "Sleeping Giant",
            "Capillarian Crest",
            "Circle of Cysquatch",
            "Bladecatcher",
            "Colony of Birchmen",
            "Hunters of the Sky",
            "Hand of Stone",
            "This Mortal Soil",
            "Siberian Divide",
            "Pendulous Skin"
        ]
    },
    {
        '_id': 4,
        'name': "Crack the Skye",
        'release_date': "2009/03/24",
        'length': "50:03",
        'labels': [
            "Reprise",
            "Relapse",
            "Sire"
        ],
        'members': [
            "Troy Sanders",
            "Brent Hinds",
            "Bill Kelliher",
            "Brann Dailor"
        ],
        'track_list': [
            "Oblivion",
            "Divinations",
            "Quintessence",
            "The Czar",
            "Ghost of Karelia",
            "Crack the Skye",
            "The Last Baron"
        ]
    },
    {
        '_id': 5,
        'name': "The Hunter",
        'release_date': "2011/09/27",
        'length': "52:54",
        'labels': [
            "Reprise",
            "Roadrunner"
        ],
        'members': [
            "Troy Sanders",
            "Brent Hinds",
            "Bill Kelliher",
            "Brann Dailor"
        ],
        'track_list': [
            "Black Tongue",
            "Curl of the Burl",
            "Blasteroid",
            "Stargasm",
            "Octopus Has No Friends",
            "All the Heavy Lifting",
            "The Hunter",
            "Dry Bone Valley",
            "Thickening",
            "Creature Lives",
            "Spectrelight",
            "Bedazzled Fingernails",
            "The Sparrow"
        ]
    },
    {
        '_id': 6,
        'name': "Once More 'Round the Sun",
        'release_date': "2014/06/24",
        'length': "54:08",
        'labels': [
            "Reprise"
        ],
        'members': [
            "Troy Sanders",
            "Brent Hinds",
            "Bill Kelliher",
            "Brann Dailor"
        ],
        'track_list': [
            "Tread Lightly",
            "The Motherload",
            "High Road",
            "Once More 'Round the Sun",
            "Chimes at Midnight",
            "Asleep in the Deep",
            "Feast Your Eyes",
            "Aunt Lisa",
            "Ember City",
            "Halloween",
            "Diamond in the Witch House"
        ]
    },
    {
        '_id': 7,
        'name': "Emperor of Sand",
        'release_date': "2017/03/31",
        'length': "51:11",
        'labels': [
            "Reprise"
        ],
        'members': [
            "Troy Sanders",
            "Brent Hinds",
            "Bill Kelliher",
            "Brann Dailor"
        ],
        'track_list': [
            "Sultan's Curse",
            "Show Yourself",
            "Precious Stones",
            "Steambreather",
            "Roots Remain",
            "Word to the Wise",
            "Ancient Kingdom",
            "Clandestiny",
            "Andromeda",
            "Scorpion Breath",
            "Jaguar God"
        ]
    },
    {
        '_id': 8,
        'name': "Hushed and Grim",
        'release_date': "2021/10/29",
        'length': "86:30",
        'labels': [
            "Reprise"
        ],
        'members': [
            "Troy Sanders",
            "Brent Hinds",
            "Bill Kelliher",
            "Brann Dailor"
        ],
        'track_list': [
            "Pain with an Anchor",
            "The Crux",
            "Sickle and Peace",
            "More Than I Could Chew",
            "The Beast",
            "Skeleton of Splendor",
            "Teardrinker",
            "Pushing the Tides",
            "Peace and Tranquility",
            "Dagger",
            "Had It All",
            "Savage Lands",
            "Gobblers of Dregs",
            "Eyes of Serpents",
            "Gigantium"
        ]
    }
]

albums_data = db.albums.insert_many(albums_list)
print(albums_data.inserted_ids)
