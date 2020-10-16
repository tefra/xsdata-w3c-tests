from dataclasses import dataclass, field
from typing import List


@dataclass
class ListType:
    """
    :ivar value:
    """
    class Meta:
        name = "list"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )


@dataclass
class Outer:
    """
    :ivar list_value:
    """
    class Meta:
        name = "outer"

    list_value: List[List[int]] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "min_occurs": 1,
            "tokens": True,
        }
    )
