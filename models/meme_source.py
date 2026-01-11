from enum import Enum, auto


class MemeSource(str, Enum):
    REDDIT = "Reddit"
    TWITTER = "Twitter"
    DEVS = "Devs"
    UNKNOWN = "Unknown"
