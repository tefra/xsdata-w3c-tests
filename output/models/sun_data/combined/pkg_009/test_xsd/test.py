from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "urn:foo"


@dataclass
class Add:
    class Meta:
        name = "add"
        namespace = "urn:foo"

    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    d: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Base:
    class Meta:
        name = "base"
        namespace = "urn:foo"

    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Default:
    class Meta:
        name = "default"
        namespace = "urn:foo"

    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class OverrideA(Enum):
    FIXED = "fixed"


@dataclass
class Prohibit:
    class Meta:
        name = "prohibit"
        namespace = "urn:foo"

    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Override:
    class Meta:
        name = "override"
        namespace = "urn:foo"

    a: Optional[OverrideA] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
