from pathlib import Path

from sizebot4 import conf
from sizebot4 import logging


class User:
	# TODO: Make slots for all various flags and values planned.
    __slots__ = ("userid", "nick", "display", "currentheight", "chu", "baseheight", "bhu", "baseweight", "bwu", "species")

    def __init__(self):
        pass

    # user.save() to save a user to the database
    def save(self):
        pass

    # User.load(userid) to load a user from the database
    @staticmethod
    def load(userid):
        pass


def getUserArray():
    pass


def setUserProperty():
    pass


def getUserFilePath(userId):
    filename = f"{userId}.txt"
    return Path(conf.user_path) / filename


def userFileExists(userId):
    path = getUserFilePath(userId)
    return path.exists()


def saveUserFile(user, data):
    userFileString = (
        f"{data['nick']}\n"
        f"{data['display']}\n"
        f"{data['currentheight']}{data['chu']}\n"
        f"{data['baseheight']}{data['bhu']}\n"
        f"{data['baseweight']}{data['bwu']}\n"
        "1.0\n"
        f"{data['species']}\n")
    path = getUserFilePath(user.id)
    with open(path, "w") as f:
        f.write(userFileString)
    logging.warn(f"Made a new user: {user}!")
    logging.log(data, timestamp=False)


def loadUserFile():
    pass


def deleteUserFile(userId):
    path = getUserFilePath(userId)
    path.unlink()
