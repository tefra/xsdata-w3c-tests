from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    class Meta:
        name = "test"

    complex_att: Optional[str] = field(
        default=None,
        metadata={
            "name": "complexAtt",
            "type": "Attribute",
        }
    )
    global_att: Optional[int] = field(
        default=None,
        metadata={
            "name": "globalAtt",
            "type": "Attribute",
        }
    )
    item1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    item2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
