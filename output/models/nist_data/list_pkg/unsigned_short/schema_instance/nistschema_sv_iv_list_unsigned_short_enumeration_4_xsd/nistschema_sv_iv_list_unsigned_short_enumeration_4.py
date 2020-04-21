from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedShort-enumeration-4-NS"


class NistschemaSvIvListUnsignedShortEnumeration4Type(Enum):
    """
    :cvar VALUE_1917_446_51111_72_39_890_745_15:
    :cvar VALUE_2777_34_2802_13_9650_13135:
    :cvar VALUE_50944_288_4230_65535_424_632_63172_6232:
    :cvar VALUE_80_1_2828_2897_8345_65535_9093:
    :cvar VALUE_80_7445_3433_28494_22_86_530_945_65535:
    :cvar VALUE_849_8668_444_9419_31_9716_28_65:
    :cvar VALUE_8759_2803_57173_193_16638_90_1173_49760_543_3457:
    """
    VALUE_1917_446_51111_72_39_890_745_15 = "1917 446 51111 72 39 890 745 15"
    VALUE_2777_34_2802_13_9650_13135 = "2777 34 2802 13 9650 13135"
    VALUE_50944_288_4230_65535_424_632_63172_6232 = "50944 288 4230 65535 424 632 63172 6232"
    VALUE_80_1_2828_2897_8345_65535_9093 = "80 1 2828 2897 8345 65535 9093"
    VALUE_80_7445_3433_28494_22_86_530_945_65535 = "80 7445 3433 28494 22 86 530 945 65535"
    VALUE_849_8668_444_9419_31_9716_28_65 = "849 8668 444 9419 31 9716 28 65"
    VALUE_8759_2803_57173_193_16638_90_1173_49760_543_3457 = "8759 2803 57173 193 16638 90 1173 49760 543 3457"


@dataclass
class NistschemaSvIvListUnsignedShortEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedShort-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-unsignedShort-enumeration-4-NS"

    value: Optional[NistschemaSvIvListUnsignedShortEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
