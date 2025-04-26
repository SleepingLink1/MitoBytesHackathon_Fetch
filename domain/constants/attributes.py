from enum import Enum

class ActivityLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Size(str, Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class Temperament(str, Enum):
    AFFECTIONATE = "Affectionate"
    ANXIOUS = "Anxious"
    ASSERTIVE = "Assertive"
    ATHLETIC = "Athletic"
    CALM = "Calm"
    CURIOUS = "Curious"
    EXCITABLE = "Excitable"
    FUNNY = "Funny"
    HAPPY = "Happy"
    LOYAL = "Loyal"
    PLAYFUL = "Playful"
    QUIET = "Quiet"
    SMART = "Smart"


class FurType(str, Enum):
    SHORT = "Short"
    MEDIUM = "Medium"
    LONG = "Long"
    CURLY = "Curly"


class IntelligenceLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class MaintenanceLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Availability(str,Enum):
    AVAILABLE = "Available"             # Currently supports adoptable dogs
    # ADOPTED = "Adopted"               # In the future will support other options
    # UNLISTED = "Unlisted"

class Sex(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

class Environment(str, Enum):
    CHILDREN = "Children"
    DOGS = "Dogs"
    CATS = "Cats"

class Age(str, Enum):
    BABY = "Baby"
    YOUNG = "Young"
    ADULT = "Adult"

