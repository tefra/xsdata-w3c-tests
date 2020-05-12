from dataclasses import dataclass, field
from typing import Optional


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
    :ivar any_element:
    :ivar a_element:
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "zing"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
    a_element: Optional[A] = field(
        default=None,
        metadata=dict(
            name="A",
            type="Element"
        )
    )
    a: Optional[A] = field(
        default=None,
        metadata=dict(
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


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
