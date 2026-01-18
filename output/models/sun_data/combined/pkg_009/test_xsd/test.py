from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

__NAMESPACE__ = "urn:foo"


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"
        namespace = "urn:foo"

    a: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    b: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    c: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class OverrideA(Enum):
    FIXED = "fixed"


@dataclass(kw_only=True)
class Add(Base):
    class Meta:
        name = "add"
        namespace = "urn:foo"

    d: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Default(Base):
    class Meta:
        name = "default"
        namespace = "urn:foo"


@dataclass(kw_only=True)
class Override(Base):
    class Meta:
        name = "override"
        namespace = "urn:foo"


@dataclass(kw_only=True)
class Prohibit(Base):
    class Meta:
        name = "prohibit"
        namespace = "urn:foo"

    c: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
