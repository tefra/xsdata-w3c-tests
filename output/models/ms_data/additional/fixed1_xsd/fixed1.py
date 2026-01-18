from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    foo: str = field(
        init=False,
        default="Ѐfixed",
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    att: str = field(
        init=False,
        default="Ѐfixed",
        metadata={
            "type": "Attribute",
        },
    )
