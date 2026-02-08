from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedInt-enumeration-4-NS"


class NistschemaSvIvListUnsignedIntEnumeration4Type(Enum):
    VALUE_11_62_582535_6677026_691306_617080803_140039_18220733_952867 = (
        11,
        62,
        582535,
        6677026,
        691306,
        617080803,
        140039,
        18220733,
        952867,
    )
    VALUE_5130_17444351_8688886_8049084_6311992 = (
        5130,
        17444351,
        8688886,
        8049084,
        6311992,
    )
    VALUE_80_990990257_91_268_196566196_34641_557310162_46453_23175 = (
        80,
        990990257,
        91,
        268,
        196566196,
        34641,
        557310162,
        46453,
        23175,
    )
    VALUE_58701769_4294967295_89715_503257427_4082_8772_1716_47104021 = (
        58701769,
        4294967295,
        89715,
        503257427,
        4082,
        8772,
        1716,
        47104021,
    )
    VALUE_82014_5521567_613030925_660302_108343_3112_4261566 = (
        82014,
        5521567,
        613030925,
        660302,
        108343,
        3112,
        4261566,
    )
    VALUE_6101_50709182_6000_2746905_38838_22141_986333_644_95 = (
        6101,
        50709182,
        6000,
        2746905,
        38838,
        22141,
        986333,
        644,
        95,
    )
    VALUE_20275407_277_234_944976672_530161667_714783900_4657401_4666020 = (
        20275407,
        277,
        234,
        944976672,
        530161667,
        714783900,
        4657401,
        4666020,
    )
    VALUE_1674452098_6209_3948525560_781_20146_4265102 = (
        1674452098,
        6209,
        3948525560,
        781,
        20146,
        4265102,
    )
    VALUE_14295_94_73497_566568265_735_519_489351607 = (
        14295,
        94,
        73497,
        566568265,
        735,
        519,
        489351607,
    )


@dataclass(kw_only=True)
class NistschemaSvIvListUnsignedIntEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedInt-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-unsignedInt-enumeration-4-NS"

    value: NistschemaSvIvListUnsignedIntEnumeration4Type = field()
