from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    AA111A2_AA = "aa111a2Aa"
    AA22_B3C = "aa22B3c"
    AA3_4 = "aa3-4_"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    val: list[S] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
