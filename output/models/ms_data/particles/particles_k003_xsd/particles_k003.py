from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    a0: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    a1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    a2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class R(B):
    a0: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    a2: Any = field(
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
