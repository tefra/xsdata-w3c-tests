from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        nillable = True

    value: None | str = field(
        default="abc",
        metadata={
            "nillable": True,
        },
    )
