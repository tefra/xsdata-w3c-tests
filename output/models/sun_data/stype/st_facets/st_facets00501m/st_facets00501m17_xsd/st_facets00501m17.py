from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ᅟ"
    A0 = "a0-ᅠ"
    A0_A = "a0Aᅡ"
    A10 = "a10ᅣ"
    A20 = "a20ᅥ"
    A30 = "a30ᅧ"
    A40 = "a40ᅩ"
    A50 = "a50ᅭ"
    A5 = "a5-ᅭ"
    A5_A = "a5Aᅮ"
    A60 = "a60ᅲ"
    A6 = "a6-ᅲ"
    A6_A = "a6Aᅳ"
    A70 = "a70ᅵ"
    A80 = "a80ᆞ"
    A90 = "a90ᆨ"


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
