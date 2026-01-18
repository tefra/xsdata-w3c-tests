from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class TestType:
    class Meta:
        name = "TEST_TYPE"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class X(TestType):
    class Meta:
        name = "x"

    any_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    a: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://test1",
        },
    )
