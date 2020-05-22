from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns-a"


@dataclass
class NsAAft:
    """
    :ivar x:
    :ivar y:
    """
    class Meta:
        name = "ns-a-aft"

    x: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=10
        )
    )
    y: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
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

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Foo:
    """
    :ivar a:
    :ivar aft:
    """
    class Meta:
        name = "foo"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    aft: Optional[NsAAft] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a"
        )
    )
