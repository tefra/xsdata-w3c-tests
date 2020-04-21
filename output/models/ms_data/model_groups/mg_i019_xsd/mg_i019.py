from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar n1_element:
    :ivar n2_element:
    :ivar n3_element:
    :ivar n4_element:
    :ivar e1:
    :ivar e2:
    :ivar e3:
    :ivar e4:
    """
    class Meta:
        name = "foo"

    n1_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://n1"
        )
    )
    n2_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://n2"
        )
    )
    n3_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://n3"
        )
    )
    n4_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://n4"
        )
    )
    e1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    e2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    e3: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    e4: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
