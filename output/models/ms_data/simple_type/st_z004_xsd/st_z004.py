from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Element1:
    """
    :ivar attribute1:
    """
    class Meta:
        name = "element1"

    attribute1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(あ|ｱ)*",
        }
    )


@dataclass
class Root:
    """
    :ivar element1:
    """
    class Meta:
        name = "root"

    element1: List[Element1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
