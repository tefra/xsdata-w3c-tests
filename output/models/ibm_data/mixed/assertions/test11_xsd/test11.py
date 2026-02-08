from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xyz"


@dataclass(kw_only=True)
class X:
    class Meta:
        namespace = "http://xyz"

    message: str = field(
        metadata={
            "type": "Element",
        }
    )
