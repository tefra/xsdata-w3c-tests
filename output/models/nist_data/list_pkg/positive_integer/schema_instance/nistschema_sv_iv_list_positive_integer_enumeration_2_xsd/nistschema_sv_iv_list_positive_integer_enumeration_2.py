from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-positiveInteger-enumeration-2-NS"


class NistschemaSvIvListPositiveIntegerEnumeration2Type(Enum):
    VALUE_5983751_77972_59447596032_46641330847161_2462139677 = (
        5983751,
        77972,
        59447596032,
        46641330847161,
        2462139677,
    )
    VALUE_4472746797959564_8497109144_5544222860625_3197643_1883940599550_736_56988114898051_7156049_85910998 = (
        4472746797959564,
        8497109144,
        5544222860625,
        3197643,
        1883940599550,
        736,
        56988114898051,
        7156049,
        85910998,
    )
    VALUE_62448830447_445591675825816_39535270562_7217115005_71471758298_4571_7977243479 = (
        62448830447,
        445591675825816,
        39535270562,
        7217115005,
        71471758298,
        4571,
        7977243479,
    )
    VALUE_517554_376071_2814760878927614_6376187700430751_2122668361011176_276024464_41573_61838791874151344_389077081 = (
        517554,
        376071,
        2814760878927614,
        6376187700430751,
        2122668361011176,
        276024464,
        41573,
        61838791874151344,
        389077081,
    )
    VALUE_20393676646704184_72201305239754_16855502465_619519727329_37830_145 = (
        20393676646704184,
        72201305239754,
        16855502465,
        619519727329,
        37830,
        145,
    )
    VALUE_70_5462344039587_833582_44719815097514_658541157127 = (
        70,
        5462344039587,
        833582,
        44719815097514,
        658541157127,
    )


@dataclass(kw_only=True)
class NistschemaSvIvListPositiveIntegerEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-positiveInteger-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-positiveInteger-enumeration-2-NS"

    value: NistschemaSvIvListPositiveIntegerEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
