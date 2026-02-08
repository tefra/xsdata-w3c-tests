from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class Computer:
    class Meta:
        name = "computer"

    cpu: str = field(
        metadata={
            "name": "CPU",
            "type": "Element",
            "namespace": "",
        }
    )
    memory: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    monitor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    speaker: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class QuietComputer(Computer):
    class Meta:
        name = "quietComputer"

    speaker: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
