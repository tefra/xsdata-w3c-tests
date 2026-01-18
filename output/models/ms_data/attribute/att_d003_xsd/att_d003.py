from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class AttRef:
    class Meta:
        name = "attRef"

    att1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 2,
            "max_length": 3,
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: None | AttRef = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
