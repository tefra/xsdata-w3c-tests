from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00వ"
    A0 = "a0-ష"
    A0_A = "a0Aహ"
    A10 = "a10ౠ"
    A1 = "a1-ౠ"
    A1_A = "a1Aౡ"
    A20 = "a20ಅ"
    A2 = "a2-ಈ"
    A2_A = "a2Aಌ"
    A30 = "a30ಎ"
    A3 = "a3-ಏ"
    A3_A = "a3Aಐ"
    A40 = "a40ಒ"
    A4 = "a4-ಝ"
    A4_A = "a4Aನ"
    A50 = "a50ಪ"
    A5 = "a5-ಮ"
    A5_A = "a5Aಳ"
    A60 = "a60ವ"
    A6 = "a6-ಷ"
    A6_A = "a6Aಹ"
    A70 = "a70ೞ"
    A80 = "a80ೠ"
    A8 = "a8-ೠ"
    A8_A = "a8Aೡ"
    A90 = "a90അ"
    A9 = "a9-ഈ"
    A9_A = "a9Aഌ"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    value: list[S] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
