from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A_1_2_3_4_5_6 = "a-1.2_3·4·5\u06dd6۞"
    A1_2_3_4_5_6_1 = "a1_2_3_4_5_6"


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
            "max_occurs": 2,
        },
    )
