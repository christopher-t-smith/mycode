#!/usr/bin/env python3
""" RPG Rooms Dictionary| Christopher T. Smith"""

rooms = {
    "Floor 1": {
        "Room 1": {
            "north": "Room 2"
        },
        "Boss Room": {
            "south": "Boss Room",
            "east": "Stairs to Floor 2"
        }
    },

    "Floor 2": {
        "Room 1": {
            "west": "Stairs to Floor 1",
            "south": "Room 2"
        },
        "Room 2": {
            "north": "Room 1",
            "east": "Room 3",
            "south": "Boss Room"
        },
        "Room 3": {
            "west": "Room 2"
        },
        "Boss Room": {
            "north": "Room 2",
            "west": "Stairs to Floor 3"
        }
    },
    
    "Floor 3": {
        "Room 1": {
            "east": "Stairs to Floor 2",
            "north": "Room 2"
        },
        "Room 2": {
            "south": "Room 1",
            "west": "Room 3"
        },
        "Room 3": {
            "east": "Room 2",
            "north": "Room 4",
            "south": "Room 5"
        },
        "Room 4": {
            "south": "Room 3",
            "west": "Boss Room"
        },
        "Room 5": {
            "north": "Room 3"
        },
        "Boss Room": {
            "east": "Room 4",
            "north": "Stairs to Floor 4"
        }
    },

    "Floor 4": {
        "Room 1": {
            "south": "Stairs to Floor 3",
            "east": "Floor 2"
         },
        "Room 2": {
            "east": "Room 1",
            "south": "Room 3"
        },
        "Room 3": {
            "north": "Room 2",
            "west": "Room 5"
        },
        "Room 4": {
            "east": "Room 3",
            "south": "Room 5",
            "north": "Room 7"
        },
        "Room 5": {
            "north": "Room 4",
            "east": "Room 6"
        },
        "Room 6": {
            "west": "Room 5",
        },
        "Room 7": {
            "south": "Room 4",
            "north": "Boss Room"
        },
        "Boss Room": {
            "south": "Room 7",
            "west": "Stairs to Floor 5"
        },
    },

    "Floor 5": {
        "Room 1": {
            "east": "Stairs to Floor 4",
            "west": "Room 2",
            "south": "Room 4"
        },
        "Room 2": {
            "east": "Room 1",
            "west": "Room 2"
        },
        "Room 3": {
            "east": "Room 2"
        },
        "Room 4": {
            "north": "Room 1",
            "west": "Room 5",
            "south": "Room 7"
        },
        "Room 5": {
            "east": "Room 4",
            "west": "Room 5"
        },
        "Room 6": {
            "east": "Room 5",
            "west": "Boss Room"
        },
        "Room 7": {
            "north": "Room 4",
            "west": "Room 8"
        },
        "Room 8": {
            "east": "Room 7",
            "west": "Room 9"
        },
        "Room 9": {
            "east": "Room 8"
        }
    }
}



