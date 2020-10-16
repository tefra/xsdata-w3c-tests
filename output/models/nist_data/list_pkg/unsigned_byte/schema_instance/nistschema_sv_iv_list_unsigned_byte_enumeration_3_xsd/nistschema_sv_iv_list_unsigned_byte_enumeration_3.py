from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-enumeration-3-NS"


class NistschemaSvIvListUnsignedByteEnumeration3Type(Enum):
    """
    :cvar VALUE_24_20_3_5_70_93:
    :cvar VALUE_255_90_31_54_41_7:
    :cvar VALUE_8_49_255_128_6_43_60_72_98:
    :cvar VALUE_16_227_86_99_255_28_3:
    :cvar VALUE_255_188_84_73_48_9_81_99:
    :cvar VALUE_41_138_91_88_63_12:
    :cvar VALUE_94_95_8_255_92_3_83:
    """
    VALUE_24_20_3_5_70_93 = "24 20 3 5 70 93"
    VALUE_255_90_31_54_41_7 = "255 90 31 54 41 7"
    VALUE_8_49_255_128_6_43_60_72_98 = "8 49 255 128 6 43 60 72 98"
    VALUE_16_227_86_99_255_28_3 = "16 227 86 99 255 28 3"
    VALUE_255_188_84_73_48_9_81_99 = "255 188 84 73 48 9 81 99"
    VALUE_41_138_91_88_63_12 = "41 138 91 88 63 12"
    VALUE_94_95_8_255_92_3_83 = "94 95 8 255 92 3 83"


@dataclass
class NistschemaSvIvListUnsignedByteEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-enumeration-3-NS"

    value: Optional[NistschemaSvIvListUnsignedByteEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
