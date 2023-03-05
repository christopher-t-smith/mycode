#!/usr/bin/env python3
""" RPG Rooms Dictionary| Christopher T. Smith"""

from basilisk import Basilisk
from dragon import Dragon
from goblin import Goblin
from golem import Golem
from ogre import Ogre
from salamander import Salamander
from skeleton import Skeleton
from slime import Slime
from troll import Troll


Rooms = {
    "Floor 1": {
        "Room 1": {
            "north": "Boss Room"
        },
        "Boss Room": {
            "south": "Room 1",
            "east": "UpStairs to Floor 2",
            "monster": Ogre()
        }
    },

    "Floor 2": {
        "Room 1": {
            "west": "DownStairs to Floor 1",
            "south": "Room 2"
        },
        "Room 2": {
            "north": "Room 1",
            "east": "Room 3",
            "south": "Boss Room",
            "monster": Slime()
        },
        "Room 3": {
            "west": "Room 2",
            "monster": Slime()
        },
        "Boss Room": {
            "north": "Room 2",
            "west": "UpStairs to Floor 3",
            "monster": Troll()
        }
    },
    
    "Floor 3": {
        "Room 1": {
            "east": "DownStairs to Floor 2",
            "north": "Room 2"
        },
        "Room 2": {
            "south": "Room 1",
            "west": "Room 3",
            "monster": Slime()
        },
        "Room 3": {
            "east": "Room 2",
            "north": "Room 4",
            "south": "Room 5",
            "monster": Goblin()
        },
        "Room 4": {
            "south": "Room 3",
            "west": "Boss Room",
            "monster": Goblin()
        },
        "Room 5": {
            "north": "Room 3",
            "monster": Slime()
        },
        "Boss Room": {
            "east": "Room 4",
            "north": "UpStairs to Floor 4",
            "monster": Golem()
        }
    },

    "Floor 4": {
        "Room 1": {
            "south": "DownStairs to Floor 3",
            "east": "Room 2"
         },
        "Room 2": {
            "east": "Room 1",
            "south": "Room 3",
            "monster": Goblin()
        },
        "Room 3": {
            "north": "Room 2",
            "west": "Room 4",
            "monster": Goblin()
        },
        "Room 4": {
            "east": "Room 3",
            "south": "Room 5",
            "north": "Room 7",
            "monster": Slime()
        },
        "Room 5": {
            "north": "Room 4",
            "east": "Room 6",
            "monster": Skeleton()
        },
        "Room 6": {
            "west": "Room 5",
            "monster": Skeleton()
        },
        "Room 7": {
            "south": "Room 4",
            "north": "Boss Room",
            "monster": Skeleton()
        },
        "Boss Room": {
            "south": "Room 7",
            "west": "UpStairs to Floor 5",
            "monster": Basilisk()
        },
    },

    "Floor 5": {
        "Room 1": {
            "east": "DownStairs to Floor 4",
            "west": "Room 2",
            "south": "Room 4"
        },
        "Room 2": {
            "east": "Room 1",
            "west": "Room 2",
            "monster": Slime()
        },
        "Room 3": {
            "east": "Room 2",
            "monster": Goblin()
        },
        "Room 4": {
            "north": "Room 1",
            "west": "Room 5",
            "south": "Room 7",
            "monster": Goblin()
        },
        "Room 5": {
            "east": "Room 4",
            "west": "Room 6",
            "monster": Salamander()
        },
        "Room 6": {
            "east": "Room 5",
            "west": "Boss Room",
            "monster": Skeleton()
        },
        "Room 7": {
            "north": "Room 4",
            "west": "Room 8",
            "monster": Salamander()
        },
        "Room 8": {
            "east": "Room 7",
            "west": "Room 9",
            "monster": Skeleton()
        },
        "Room 9": {
            "east": "Room 8",
            "monster": Salamander()
        },
        "Boss Room": {
            "east": "Room 6",
            "monster": Dragon()
        }
    }
}



