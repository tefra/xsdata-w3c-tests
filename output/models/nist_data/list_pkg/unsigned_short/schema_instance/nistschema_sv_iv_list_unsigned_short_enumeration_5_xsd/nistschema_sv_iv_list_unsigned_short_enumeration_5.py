from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedShort-enumeration-5-NS"


class NistschemaSvIvListUnsignedShortEnumeration5Type(Enum):
    """
    :cvar VALUE_1195_882_287_134_3503_7711_2881_3695:
    :cvar VALUE_20_65535_9047_2842_5871_69_4364:
    :cvar VALUE_47_7223_1_50_12_1674_34775_159_951:
    :cvar VALUE_65535_19223_772_44_97:
    :cvar VALUE_8_60_964_225_90_485_9105:
    :cvar VALUE_9186_243_2499_26_29_54_967_315_35168_1660:
    """
    VALUE_1195_882_287_134_3503_7711_2881_3695 = "1195 882 287 134 3503 7711 2881 3695"
    VALUE_20_65535_9047_2842_5871_69_4364 = "20 65535 9047 2842 5871 69 4364"
    VALUE_47_7223_1_50_12_1674_34775_159_951 = "47 7223 1 50 12 1674 34775 159 951"
    VALUE_65535_19223_772_44_97 = "65535 19223 772 44 97"
    VALUE_8_60_964_225_90_485_9105 = "8 60 964 225 90 485 9105"
    VALUE_9186_243_2499_26_29_54_967_315_35168_1660 = "9186 243 2499 26 29 54 967 315 35168 1660"


@dataclass
class NistschemaSvIvListUnsignedShortEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedShort-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-unsignedShort-enumeration-5-NS"

    value: Optional[NistschemaSvIvListUnsignedShortEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
