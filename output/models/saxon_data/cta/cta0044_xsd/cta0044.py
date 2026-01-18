from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "abc"


@dataclass(kw_only=True)
class AType:
    class Meta:
        name = "aType"

    t: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "abc",
        },
    )
    f: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "abc",
        },
    )
    switch: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    r: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class A(AType):
    class Meta:
        name = "a"
        namespace = "abc"


@dataclass(kw_only=True)
class ATypeF(AType):
    class Meta:
        name = "aType_f"

    t: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    f: str = field(
        metadata={
            "type": "Element",
            "namespace": "abc",
            "required": True,
        }
    )
    r: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class ATypeT(AType):
    class Meta:
        name = "aType_t"

    f: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    t: str = field(
        metadata={
            "type": "Element",
            "namespace": "abc",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Top:
    class Meta:
        name = "top"
        namespace = "abc"

    a: A = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
