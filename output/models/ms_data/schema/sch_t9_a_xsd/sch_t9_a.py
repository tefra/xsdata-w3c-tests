from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns-a"


@dataclass
class ACt:
    """
    :ivar att1:
    :ivar att2:
    """
    class Meta:
        name = "A-ct"

    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att2: str = field(
        default="bar",
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class E2:
    """
    :ivar value:
    """
    class Meta:
        name = "e2"
        namespace = "ns-a"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            total_digits=2
        )
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ns-a"

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
class E1(ACt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
