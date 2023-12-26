from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    class Meta:
        name = "test"

    global_att: Optional[int] = field(
        default=None,
        metadata={
            "name": "globalAtt",
            "type": "Attribute",
        },
    )
