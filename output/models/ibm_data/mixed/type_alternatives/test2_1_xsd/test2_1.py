from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Example:
    x: List[Union["Example.KindQuantity", "Example.KindPrice", "Example.KindMesg"]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class KindQuantity:
        value: Optional[int] = field(
            default=None,
        )
        kind: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class KindPrice:
        value: Optional[float] = field(
            default=None,
        )
        kind: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class KindMesg:
        value: Optional[str] = field(
            default=None,
        )
        kind: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
