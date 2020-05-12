from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A1_2_3_4_5_6:
    :cvar A_1_2_3_4_5_6:
    """
    A1_2_3_4_5_6 = "a1_2_3_4_5_6"
    A_1_2_3_4_5_6 = "a-1.2_3·4·5۝6۞"


@dataclass
class Root:
    """
    :ivar val:
    """
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    val: List[S] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=2
        )
    )
