from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    complex_att: None | str = field(
        default=None,
        metadata={
            "name": "complexAtt",
            "type": "Attribute",
        },
    )
    global_att: None | int = field(
        default=None,
        metadata={
            "name": "globalAtt",
            "type": "Attribute",
        },
    )
    item1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    item2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
