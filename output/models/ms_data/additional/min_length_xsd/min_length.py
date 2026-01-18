from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    foo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 6,
        },
    )
    att: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 6,
        },
    )
