from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class B:
    target001_com_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.target001.com/",
        },
    )


@dataclass(kw_only=True)
class R(B):
    target001_com_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    child: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.target001.com/",
        }
    )


@dataclass(kw_only=True)
class Parent(R):
    class Meta:
        name = "parent"
