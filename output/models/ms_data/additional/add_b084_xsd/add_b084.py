from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
