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
        


