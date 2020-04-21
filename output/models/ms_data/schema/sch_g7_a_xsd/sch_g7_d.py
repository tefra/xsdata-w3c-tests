from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-d"


@dataclass
class CtA:
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "ct-A"

    a1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    a2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Foo:
    """
    :ivar any_element:
    """
    class Meta:
        name = "foo"
        namespace = "ns-d"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class E1(CtA):
    class Meta:
        name = "e1"
        namespace = "ns-d"
