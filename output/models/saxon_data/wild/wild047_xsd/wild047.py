from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class Computer1:
    class Meta:
        name = "computer"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    local_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "max_occurs": 2,
            "process_contents": "skip",
        },
    )
    extra_com_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://extra.com/",
            "max_occurs": 2,
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class RestrictedComputer(Computer1):
    class Meta:
        name = "restrictedComputer"

    extra_com_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Computer(RestrictedComputer):
    class Meta:
        name = "computer"
