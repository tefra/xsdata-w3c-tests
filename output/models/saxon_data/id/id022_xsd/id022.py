from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Para:
    """
    :ivar value:
    :ivar key:
    :ivar ref:
    """
    class Meta:
        name = "para"

    value: Optional[str] = field(
        default=None,
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    ref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Doc:
    """
    :ivar para:
    """
    class Meta:
        name = "doc"

    para: List[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
