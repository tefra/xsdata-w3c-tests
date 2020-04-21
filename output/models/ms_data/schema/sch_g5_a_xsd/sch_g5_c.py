from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-b"


@dataclass
class CtC:
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "ct-C"

    a1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    a2: Optional[int] = field(
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
        namespace = "ns-b"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class E3(CtC):
    class Meta:
        name = "e3"
        namespace = "ns-b"
