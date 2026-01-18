from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "b"


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"

    b: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "b",
        },
    )
