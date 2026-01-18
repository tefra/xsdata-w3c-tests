from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class B:
    target003_com_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.target003.com/",
        },
    )


@dataclass(kw_only=True)
class R(B):
    target003_com_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    att: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.target003.com/",
        },
    )


@dataclass(kw_only=True)
class Parent(R):
    class Meta:
        name = "parent"
