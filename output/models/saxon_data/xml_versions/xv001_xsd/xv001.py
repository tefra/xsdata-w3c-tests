from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class DKstra:
    class Meta:
        name = "Dĳkstra"

    vr_tag: bool = field(
        metadata={
            "name": "vrĳtag",
            "type": "Attribute",
            "required": True,
        }
    )
