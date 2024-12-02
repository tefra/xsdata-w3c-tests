from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ஂ"
    A0 = "a0-ஂ"
    A0_A = "a0Aஃ"
    A10 = "a10ா"
    A1 = "a1-ீ"
    A1_A = "a1Aூ"
    A20 = "a20ெ"
    A2 = "a2-ே"
    A2_A = "a2Aை"
    A30 = "a30ொ"
    A3 = "a3-ோ"
    A3_A = "a3A்"
    A40 = "a40ௗ"
    A50 = "a50ఁ"
    A5 = "a5-ం"
    A5_A = "a5Aః"
    A60 = "a60ా"
    A6 = "a6-ు"
    A6_A = "a6Aౄ"
    A70 = "a70ె"
    A7 = "a7-ే"
    A7_A = "a7Aై"
    A80 = "a80ొ"
    A8 = "a8-ో"
    A8_A = "a8A్"
    A90 = "a90ౕ"
    A9 = "a9-ౕ"
    A9_A = "a9Aౖ"


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
