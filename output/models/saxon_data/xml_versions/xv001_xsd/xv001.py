from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DKstra:
    """
    :ivar vr_tag:
    """
    class Meta:
        name = "Dĳkstra"

    vr_tag: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="vrĳtag",
            type="Attribute",
            required=True
        )
    )
