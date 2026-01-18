from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "d"


@dataclass(kw_only=True)
class D:
    class Meta:
        name = "d"

    d: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "d",
        },
    )
