from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A:
    """
    :ivar any_element:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Zing:
    """
    :ivar a:
    :ivar a_element:
    :ivar b:
    :ivar c:
    :ivar any_element:
    """
    class Meta:
        name = "zing"

    a: Optional[A] = field(
        default=None,
        metadata=dict(
            name="A",
            type="Element"
        )
    )
    a_element: Optional[A] = field(
        default=None,
        metadata=dict(
            name="a",
            type="Element"
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    c: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
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
class Root(Zing):
    class Meta:
        name = "root"
