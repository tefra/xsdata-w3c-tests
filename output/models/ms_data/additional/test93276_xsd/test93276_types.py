from enum import Enum

__NAMESPACE__ = "foo"


class GlobalAddressTypeValues(Enum):
    MA = "MA"
    PH = "PH"


class GlobalNameTypeValues(Enum):
    LG = "LG"
    DB = "DB"


class GlobalSimpleStatusType(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class GlobalYesNoType(Enum):
    Y = "Y"
    N = "N"
