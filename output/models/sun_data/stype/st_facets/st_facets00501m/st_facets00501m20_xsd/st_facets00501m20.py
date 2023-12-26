from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00Ὓ"
    A10 = "a10Ὕ"
    A20 = "a20Ὗ"
    A2 = "a2-Ὦ"
    A2_A = "a2Aώ"
    A30 = "a30ᾰ"
    A3 = "a3-ᾰ"
    A3_A = "a3Aᾱ"
    A40 = "a40Ᾰ"
    A4 = "a4-Ᾱ"
    A4_A = "a4AΆ"
    A50 = "a50Ὲ"
    A5 = "a5-Έ"
    A5_A = "a5AΉ"
    A60 = "a60ῐ"
    A6 = "a6-ῐ"
    A6_A = "a6Aῑ"
    A70 = "a70Ῐ"
    A7 = "a7-Ῑ"
    A7_A = "a7AΊ"
    A80 = "a80ῠ"
    A8 = "a8-ῠ"
    A8_A = "a8Aῡ"
    A90 = "a90ῥ"


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
