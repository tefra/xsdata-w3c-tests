from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class CtA:
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "ct-A"

    a1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    a2: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class E1(CtA):
    class Meta:
        name = "e1"
