from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ᆫ"
    A10 = "a10ᆮ"
    A1 = "a1-ᆮ"
    A1_A = "a1Aᆯ"
    A20 = "a20ᆷ"
    A2 = "a2-ᆷ"
    A2_A = "a2Aᆸ"
    A30 = "a30ᆺ"
    A40 = "a40ᆼ"
    A4 = "a4-ᆿ"
    A4_A = "a4Aᇂ"
    A50 = "a50ᇫ"
    A60 = "a60ᇰ"
    A70 = "a70ᇹ"
    A80 = "a80Ḁ"
    A8 = "a8-Ṋ"
    A8_A = "a8Aẕ"
    A90 = "a90ẛ"


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
