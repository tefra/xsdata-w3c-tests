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
    :cvar LG:
    :cvar DB:
    """
    LG = "LG"
    DB = "DB"


class GlobalSimpleStatusType(Enum):
    """
    :cvar VALUE_0:
    :cvar VALUE_1:
    """
    VALUE_0 = "0"
    VALUE_1 = "1"


class GlobalYesNoType(Enum):
    """
    :cvar Y:
    :cvar N:
    """
    Y = "Y"
    N = "N"
