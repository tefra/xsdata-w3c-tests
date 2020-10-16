from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Appendix:
    """
    :ivar value:
    :ivar type:
    """
    class Meta:
        name = "appendix"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Chap:
    """
    :ivar value:
    :ivar type:
    """
    class Meta:
        name = "chap"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Doc:
    """
    :ivar appendix:
    :ivar chap:
    """
    class Meta:
        name = "doc"

    appendix: List[Appendix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    chap: List[Chap] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
