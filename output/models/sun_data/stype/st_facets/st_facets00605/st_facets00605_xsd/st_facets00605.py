from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_0:
    :cvar VALUE:
    """
    VALUE_0 = "_-0."
    VALUE = "_-."


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
