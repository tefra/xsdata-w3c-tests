from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ਓ"
    A0 = "a0-ਝ"
    A0_A = "a0Aਨ"
    A10 = "a10ਪ"
    A1 = "a1-ਭ"
    A1_A = "a1Aਰ"
    A20 = "a20ਲ"
    A2 = "a2-ਲ"
    A2_A = "a2Aਲ਼"
    A30 = "a30ਵ"
    A3 = "a3-ਵ"
    A3_A = "a3Aਸ਼"
    A40 = "a40ਸ"
    A4 = "a4-ਸ"
    A4_A = "a4Aਹ"
    A50 = "a50ਖ਼"
    A5 = "a5-ਗ਼"
    A5_A = "a5Aੜ"
    A60 = "a60ਫ਼"
    A70 = "a70ੲ"
    A7 = "a7-ੳ"
    A7_A = "a7Aੴ"
    A80 = "a80અ"
    A8 = "a8-ઈ"
    A8_A = "a8Aઋ"
    A90 = "a90ઍ"


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
