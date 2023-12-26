from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedLong-enumeration-5-NS"


class NistschemaSvIvListUnsignedLongEnumeration5Type(Enum):
    VALUE_273391265688431417_4912349661069_114679349477691761_18072221934_7751931171_67999400860626280_44533922895279165_19619_824189070610064 = (
        273391265688431417,
        4912349661069,
        114679349477691761,
        18072221934,
        7751931171,
        67999400860626280,
        44533922895279165,
        19619,
        824189070610064,
    )
    VALUE_659_52327731590451_89270818934010_3913500432_4597432388225450_6987149198957_7341038702279596 = (
        659,
        52327731590451,
        89270818934010,
        3913500432,
        4597432388225450,
        6987149198957,
        7341038702279596,
    )
    VALUE_1187898961393_20304679_909078993672614_73742683626273_2260_40_3291130_831 = (
        1187898961393,
        20304679,
        909078993672614,
        73742683626273,
        2260,
        40,
        3291130,
        831,
    )
    VALUE_8402945834710476_88_49556782534514_29648533_91134 = (
        8402945834710476,
        88,
        49556782534514,
        29648533,
        91134,
    )
    VALUE_867155510362_26926603524_803635144_83750110563063_870791928904_7352_7346_4287874_6195 = (
        867155510362,
        26926603524,
        803635144,
        83750110563063,
        870791928904,
        7352,
        7346,
        4287874,
        6195,
    )
    VALUE_889926817263871_7378_2538_63652306446909_674090_95647 = (
        889926817263871,
        7378,
        2538,
        63652306446909,
        674090,
        95647,
    )


@dataclass
class NistschemaSvIvListUnsignedLongEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedLong-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-unsignedLong-enumeration-5-NS"

    value: Optional[NistschemaSvIvListUnsignedLongEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
