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
    CALM = "Calm"
    EXCITABLE = "Excitable"
    ANXIOUS = "Anxious"
    ASSERTIVE = "Assertive"


class FurType(str, Enum):
    NONE = "None"
    SHORT = "Short"
    MEDIUM = "Medium"
    LONG = "Long"


class IntelligenceLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class MaintenanceLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    
class Availability(str,Enum):
    AVAILABLE = "Available"
    ADOPTED = "Adopted"
    UNLISTED = "Unlisted"
    
class Sex(str, Enum):
    MALE = "Male"
    FEMALE = "Female"