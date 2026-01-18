from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class C:
    class Meta:
        name = "c"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    x: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    y: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class D(C):
    class Meta:
        name = "d"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    p: D = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
