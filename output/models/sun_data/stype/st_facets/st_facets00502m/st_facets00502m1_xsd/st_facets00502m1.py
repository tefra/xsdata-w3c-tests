from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00一"
    A0 = "a0-盒"
    A0_A = "a0A龥"
    A10 = "a10〇"
    A20 = "a20〡"
    A2 = "a2-〥"
    A2_A = "a2A〩"


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
