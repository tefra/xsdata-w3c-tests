from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class AttgRef:
    class Meta:
        name = "attgRef"

    att1: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: None | AttgRef = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
