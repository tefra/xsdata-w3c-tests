from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    global_att: None | int = field(
        default=None,
        metadata={
            "name": "globalAtt",
            "type": "Attribute",
        },
    )
