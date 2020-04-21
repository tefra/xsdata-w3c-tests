from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "abc"


@dataclass
class AType:
    """
    :ivar t:
    :ivar f:
    :ivar switch:
    :ivar r:
    """
    class Meta:
        name = "aType"

    t: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="abc"
        )
    )
    f: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="abc"
        )
    )
    switch: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    r: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class ATypeF:
    """
    :ivar t:
    :ivar f:
    :ivar switch:
    :ivar r:
    """
    class Meta:
        name = "aType_f"

    t: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="abc"
        )
    )
    f: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="abc",
            required=True
        )
    )
    switch: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    r: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class ATypeT:
    """
    :ivar t:
    :ivar f:
    :ivar switch:
    :ivar r:
    """
    class Meta:
        name = "aType_t"

    t: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="abc",
            required=True
        )
    )
    f: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="abc"
        )
    )
    switch: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    r: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class A(AType):
    class Meta:
        name = "a"
        namespace = "abc"



@dataclass
class Top:
    """
    :ivar a:
    """
    class Meta:
        name = "top"
        namespace = "abc"

    a: Optional[A] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
