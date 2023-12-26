from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ஜ"
    A10 = "a10ஞ"
    A1 = "a1-ஞ"
    A1_A = "a1Aட"
    A20 = "a20ண"
    A2 = "a2-ண"
    A2_A = "a2Aத"
    A30 = "a30ந"
    A3 = "a3-ன"
    A3_A = "a3Aப"
    A40 = "a40ம"
    A4 = "a4-ற"
    A4_A = "a4Aவ"
    A50 = "a50ஷ"
    A5 = "a5-ஸ"
    A5_A = "a5Aஹ"
    A60 = "a60అ"
    A6 = "a6-ఈ"
    A6_A = "a6Aఌ"
    A70 = "a70ఎ"
    A7 = "a7-ఏ"
    A7_A = "a7Aఐ"
    A80 = "a80ఒ"
    A8 = "a8-ఝ"
    A8_A = "a8Aన"
    A90 = "a90ప"
    A9 = "a9-మ"
    A9_A = "a9Aళ"


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
