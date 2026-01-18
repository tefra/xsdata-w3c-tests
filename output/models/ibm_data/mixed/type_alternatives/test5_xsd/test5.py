from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class X:
    a: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    b: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    d: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    minimal: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Y(X):
    c: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    d: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    a: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Test(X):
    class Meta:
        name = "test"
