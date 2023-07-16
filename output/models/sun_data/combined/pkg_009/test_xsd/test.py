from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Any

__NAMESPACE__ = "urn:foo"


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


class OverrideA(Enum):
    FIXED = "fixed"


@dataclass
class Add(Base):
    class Meta:
        name = "add"
        namespace = "urn:foo"

    d: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Default(Base):
    class Meta:
        name = "default"
        namespace = "urn:foo"


@dataclass
class Override(Base):
    class Meta:
        name = "override"
        namespace = "urn:foo"


@dataclass
class Prohibit(Base):
    class Meta:
        name = "prohibit"
        namespace = "urn:foo"

    c: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        }
    )
