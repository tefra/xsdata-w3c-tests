from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-enumeration-5-NS"


class NistschemaSvIvListUnsignedByteEnumeration5Type(Enum):
    """
    :cvar VALUE_24_89_96_33_146_92_255_65_211:
    :cvar VALUE_22_255_43_91_77_50_20_70_93:
    :cvar VALUE_98_16_255_31_61_4_73_57_51:
    :cvar VALUE_9_93_65_4_255_45_52_70:
    :cvar VALUE_255_75_86_65_4_56:
    :cvar VALUE_255_71_8_66_13_98_59:
    :cvar VALUE_97_21_29_255_6_75_8_31_14:
    :cvar VALUE_6_28_49_24_61_255_92_66:
    :cvar VALUE_7_8_92_74_61_223_59_76_65:
    :cvar VALUE_90_6_255_67_46_36_86_99:
    """
    VALUE_24_89_96_33_146_92_255_65_211 = "24 89 96 33 146 92 255 65 211"
    VALUE_22_255_43_91_77_50_20_70_93 = "22 255 43 91 77 50 20 70 93"
    VALUE_98_16_255_31_61_4_73_57_51 = "98 16 255 31 61 4 73 57 51"
    VALUE_9_93_65_4_255_45_52_70 = "9 93 65 4 255 45 52 70"
    VALUE_255_75_86_65_4_56 = "255 75 86 65 4 56"
    VALUE_255_71_8_66_13_98_59 = "255 71 8 66 13 98 59"
    VALUE_97_21_29_255_6_75_8_31_14 = "97 21 29 255 6 75 8 31 14"
    VALUE_6_28_49_24_61_255_92_66 = "6 28 49 24 61 255 92 66"
    VALUE_7_8_92_74_61_223_59_76_65 = "7 8 92 74 61 223 59 76 65"
    VALUE_90_6_255_67_46_36_86_99 = "90 6 255 67 46 36 86 99"


@dataclass
class NistschemaSvIvListUnsignedByteEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-enumeration-5-NS"

    value: Optional[NistschemaSvIvListUnsignedByteEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
