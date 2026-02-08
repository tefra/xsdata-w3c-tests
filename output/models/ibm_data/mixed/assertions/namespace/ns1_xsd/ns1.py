from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.example.org"


@dataclass(kw_only=True)
class X:
    class Meta:
        name = "x"
        namespace = "http://www.example.org"

    y: str = field(
        metadata={
            "type": "Element",
        }
    )
