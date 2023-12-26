from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ᄋ"
    A0 = "a0-ᄋ"
    A0_A = "a0Aᄌ"
    A10 = "a10ᄎ"
    A1 = "a1-ᄐ"
    A1_A = "a1Aᄒ"
    A20 = "a20ᄼ"
    A30 = "a30ᄾ"
    A40 = "a40ᅀ"
    A50 = "a50ᅌ"
    A60 = "a60ᅎ"
    A70 = "a70ᅐ"
    A80 = "a80ᅔ"
    A8 = "a8-ᅔ"
    A8_A = "a8Aᅕ"
    A90 = "a90ᅙ"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    value: List[S] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
