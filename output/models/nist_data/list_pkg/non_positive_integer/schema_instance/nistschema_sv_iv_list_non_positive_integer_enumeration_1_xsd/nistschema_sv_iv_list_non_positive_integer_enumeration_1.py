from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonPositiveInteger-enumeration-1-NS"


class NistschemaSvIvListNonPositiveIntegerEnumeration1Type(Enum):
    VALUE_806173204231161_43189_633999400782_3727116_67366_79_5334724745 = (
        -806173204231161,
        -43189,
        -633999400782,
        -3727116,
        -67366,
        -79,
        -5334724745,
    )
    VALUE_25641_239_725_668477_6600005219897289 = (
        -25641,
        -239,
        -725,
        -668477,
        -6600005219897289,
    )
    VALUE_540978747_856555_1904280701_4756829_750155027_11096_445_50930676365418914_64462511088_9375938 = (
        -540978747,
        -856555,
        -1904280701,
        -4756829,
        -750155027,
        -11096,
        -445,
        -50930676365418914,
        -64462511088,
        -9375938,
    )
    VALUE_766_852457_690633319_80335063204687651_917_96776242453_2281 = (
        -766,
        -852457,
        -690633319,
        -80335063204687651,
        -917,
        -96776242453,
        -2281,
    )
    VALUE_829190862581_36227178_36889641_67489463641462488_161_93974534575426982_8049302376462250 = (
        -829190862581,
        -36227178,
        -36889641,
        -67489463641462488,
        -161,
        -93974534575426982,
        -8049302376462250,
    )
    VALUE_936_28721786542842_678_45820753_11_9048231986289267 = (
        -936,
        -28721786542842,
        -678,
        -45820753,
        -11,
        -9048231986289267,
    )
    VALUE_15_2258372883401_676672894181550_949319651303_984 = (
        -15,
        -2258372883401,
        -676672894181550,
        -949319651303,
        -984,
    )


@dataclass
class NistschemaSvIvListNonPositiveIntegerEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonPositiveInteger-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-nonPositiveInteger-enumeration-1-NS"

    value: Optional[NistschemaSvIvListNonPositiveIntegerEnumeration1Type] = (
        field(
            default=None,
            metadata={
                "required": True,
            },
        )
    )
