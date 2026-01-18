from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    e1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
    e2: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 3,
        },
    )
    e3: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 3,
        },
    )


@dataclass(kw_only=True)
class R(B):
    e2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    e3: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | R = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
