from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-byte-enumeration-3-NS"


class NistschemaSvIvListByteEnumeration3Type(Enum):
    """
    :cvar VALUE_128_127_19_99_72_65_4_81_74:
    :cvar VALUE_4_19_38_52_98_34_127_8_128:
    :cvar VALUE_66_51_7_9_127_23_54:
    :cvar VALUE_127_22_82_5_94:
    :cvar VALUE_27_127_4_71_64_128_68:
    :cvar VALUE_3_99_3_42_37_64_56:
    :cvar VALUE_89_128_5_50_35_127_57:
    :cvar VALUE_89_93_46_55_32_78_79:
    :cvar VALUE_9_69_99_72_38_128:
    """
    VALUE_128_127_19_99_72_65_4_81_74 = "-128 127 19 99 72 -65 -4 -81 74"
    VALUE_4_19_38_52_98_34_127_8_128 = "-4 19 38 52 -98 34 127 -8 -128"
    VALUE_66_51_7_9_127_23_54 = "-66 51 -7 -9 127 -23 54"
    VALUE_127_22_82_5_94 = "127 22 -82 5 94"
    VALUE_27_127_4_71_64_128_68 = "27 127 -4 71 64 -128 -68"
    VALUE_3_99_3_42_37_64_56 = "3 99 -3 -42 37 -64 56"
    VALUE_89_128_5_50_35_127_57 = "89 -128 5 -50 35 127 -57"
    VALUE_89_93_46_55_32_78_79 = "89 93 46 -55 -32 -78 -79"
    VALUE_9_69_99_72_38_128 = "9 -69 -99 -72 38 -128"


@dataclass
class NistschemaSvIvListByteEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-byte-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-byte-enumeration-3-NS"

    value: Optional[NistschemaSvIvListByteEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
