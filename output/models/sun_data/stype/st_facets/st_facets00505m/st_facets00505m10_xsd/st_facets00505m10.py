from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00⃐"
    A0 = "a0-⃖"
    A0_A = "a0A⃜"
    A10 = "a10⃡"
    A20 = "a20〪"
    A2 = "a2-〬"
    A2_A = "a2A〯"
    A30 = "a30゙"
    A40 = "a40゚"


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
