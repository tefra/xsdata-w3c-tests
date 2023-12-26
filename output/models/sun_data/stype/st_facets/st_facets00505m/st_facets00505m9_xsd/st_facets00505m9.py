from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00༹"
    A10 = "a10༾"
    A20 = "a20༿"
    A30 = "a30ཱ"
    A3 = "a3-ེ"
    A3_A = "a3A྄"
    A40 = "a40྆"
    A4 = "a4-྆"
    A4_A = "a4A྇"
    A50 = "a50ྐ"
    A5 = "a5-ྒ"
    A5_A = "a5Aྕ"
    A60 = "a60ྗ"
    A70 = "a70ྙ"
    A7 = "a7-ྣ"
    A7_A = "a7Aྭ"
    A80 = "a80ྱ"
    A8 = "a8-ྴ"
    A8_A = "a8Aྷ"
    A90 = "a90ྐྵ"


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
