from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ٰ"
    A10 = "a10ۖ"
    A1 = "a1-ۙ"
    A1_A = "a1Aۜ"
    A20 = "a20۝"
    A2 = "a2-۞"
    A2_A = "a2A۟"
    A30 = "a30۠"
    A3 = "a3-ۢ"
    A3_A = "a3Aۤ"
    A40 = "a40ۧ"
    A4 = "a4-ۧ"
    A4_A = "a4Aۨ"
    A50 = "a50۪"
    A5 = "a5-۫"
    A5_A = "a5Aۭ"
    A60 = "a60ँ"
    A6 = "a6-ं"
    A6_A = "a6Aः"
    A70 = "a70़"
    A80 = "a80ा"
    A8 = "a8-ॅ"
    A8_A = "a8Aौ"
    A90 = "a90्"


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
