from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ະ"
    A10 = "a10າ"
    A1 = "a1-າ"
    A1_A = "a1Aຳ"
    A20 = "a20ຽ"
    A30 = "a30ເ"
    A3 = "a3-ໂ"
    A3_A = "a3Aໄ"
    A40 = "a40ཀ"
    A4 = "a4-གྷ"
    A4_A = "a4Aཇ"
    A50 = "a50ཉ"
    A5 = "a5-ཙ"
    A5_A = "a5Aཀྵ"
    A60 = "a60ᄀ"
    A70 = "a70ᄂ"
    A7 = "a7-ᄂ"
    A7_A = "a7Aᄃ"
    A80 = "a80ᄅ"
    A8 = "a8-ᄆ"
    A8_A = "a8Aᄇ"
    A90 = "a90ᄉ"


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
        }
    )
