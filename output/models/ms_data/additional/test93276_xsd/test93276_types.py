from enum import Enum

__NAMESPACE__ = "foo"


class GlobalAddressTypeValues(Enum):
    """
    :cvar MA:
    :cvar PH:
    """
    MA = "MA"
    PH = "PH"


class GlobalNameTypeValues(Enum):
    """
    :cvar DB:
    :cvar LG:
    """
    DB = "DB"
    LG = "LG"


class GlobalSimpleStatusType(Enum):
    """
    :cvar VALUE_0:
    :cvar VALUE_1:
    """
    VALUE_0 = "0"
    VALUE_1 = "1"


class GlobalYesNoType(Enum):
    """
    :cvar N:
    :cvar Y:
    """
    N = "N"
    Y = "Y"
