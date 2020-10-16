from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Regex:
    """
    :ivar att:
    """
    att: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*",
        }
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: List[Regex] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
