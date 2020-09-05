from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "urn:foo"


@dataclass
class Add:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar d:
    """
    class Meta:
        name = "add"
        namespace = "urn:foo"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    c: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    d: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Base:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "base"
        namespace = "urn:foo"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    c: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class Default:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "default"
        namespace = "urn:foo"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    c: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Override:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "override"
        namespace = "urn:foo"

    a: Optional["Override.A"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    c: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class A(Enum):
        """
        :cvar FIXED:
        """
        FIXED = "fixed"


@dataclass
class Prohibit:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "prohibit"
        namespace = "urn:foo"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    c: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
