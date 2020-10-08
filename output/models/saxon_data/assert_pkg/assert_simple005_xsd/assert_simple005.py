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
        metadata=dict(
            tokens=True
        )
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
        metadata=dict(
            name="list",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807,
            tokens=True
        )
    )
