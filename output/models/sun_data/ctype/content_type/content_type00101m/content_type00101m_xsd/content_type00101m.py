from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "contentType"


@dataclass(kw_only=True)
class A1:
    class Meta:
        name = "A"

    attr1: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class A(A1):
    class Meta:
        name = "a"
        namespace = "contentType"
