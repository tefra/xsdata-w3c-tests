from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_01:
    :cvar VALUE_02:
    :cvar VALUE_MINUS_2:
    :cvar A2:
    :cvar VALUE_00:
    :cvar VALUE_MINUS_0:
    :cvar A0:
    """
    VALUE_01 = "〇01"
    VALUE_02 = "〡02"
    VALUE_MINUS_2 = "〥-2"
    A2 = "〩a2"
    VALUE_00 = "一00"
    VALUE_MINUS_0 = "盒-0"
    A0 = "龥a0"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    value: List[S] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
