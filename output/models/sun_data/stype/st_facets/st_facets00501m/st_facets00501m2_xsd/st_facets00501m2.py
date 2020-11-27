from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00Ŋ"
    A0 = "a0-Ť"
    A0_A = "a0Až"
    A10 = "a10ƀ"
    A1 = "a1-Ɗ"
    A1_A = "a1AƔ"
    A20 = "a20Ɩ"
    A2 = "a2-Ɲ"
    A2_A = "a2Aƥ"
    A30 = "a30Ƨ"
    A3 = "a3-ƨ"
    A3_A = "a3AƩ"
    A40 = "a40ƫ"
    A4 = "a4-ƴ"
    A4_A = "a4Aƽ"
    A50 = "a50ǀ"
    A5 = "a5-ǁ"
    A5_A = "a5Aǃ"
    A60 = "a60Ǎ"
    A6 = "a6-Ǟ"
    A6_A = "a6Aǯ"
    A70 = "a70Ǵ"
    A7 = "a7-Ǵ"
    A7_A = "a7Aǵ"
    A80 = "a80Ǻ"
    A8 = "a8-Ȉ"
    A8_A = "a8Aȗ"
    A90 = "a90ɐ"
    A9 = "a9-ɢ"
    A9_A = "a9Aɴ"


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
