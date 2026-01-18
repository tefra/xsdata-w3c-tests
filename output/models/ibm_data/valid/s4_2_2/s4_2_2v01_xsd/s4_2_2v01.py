from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    ele11: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
