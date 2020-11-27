from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DKstra:
    class Meta:
        name = "Dĳkstra"

    vr_tag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "vrĳtag",
            "type": "Attribute",
            "required": True,
        }
    )
