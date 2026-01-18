from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-short-enumeration-3-NS"


class NistschemaSvIvListShortEnumeration3Type(Enum):
    VALUE_959_31_743_6_56_3_182_4697_48_67 = (
        959,
        31,
        743,
        -6,
        -56,
        -3,
        182,
        -4697,
        -48,
        67,
    )
    VALUE_9594_6640_616_745_32768_525_42_26747_2118_67 = (
        -9594,
        -6640,
        -616,
        745,
        -32768,
        -525,
        -42,
        26747,
        -2118,
        -67,
    )
    VALUE_674_26883_97_32767_878_32768_257 = (
        -674,
        26883,
        -97,
        32767,
        -878,
        -32768,
        257,
    )
    VALUE_8_53_21_8232_5211_333_108_24 = (
        8,
        53,
        21,
        -8232,
        -5211,
        333,
        108,
        -24,
    )
    VALUE_686_956_207_15_9007_32768_32767_53 = (
        -686,
        956,
        207,
        15,
        -9007,
        -32768,
        32767,
        53,
    )
    VALUE_8901_66_24875_7604_6_6037_738 = (
        8901,
        66,
        24875,
        7604,
        -6,
        -6037,
        -738,
    )


@dataclass(kw_only=True)
class NistschemaSvIvListShortEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-short-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-short-enumeration-3-NS"

    value: NistschemaSvIvListShortEnumeration3Type = field(
        metadata={
            "required": True,
        }
    )
