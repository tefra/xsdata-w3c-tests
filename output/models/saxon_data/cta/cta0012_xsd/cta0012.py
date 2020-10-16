from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Chap:
    """
    :ivar de:
    :ivar fr:
    :ivar en:
    """
    class Meta:
        name = "chap"

    de: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    fr: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    en: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Doc:
    """
    :ivar chap:
    :ivar lang:
    """
    class Meta:
        name = "doc"

    chap: List[Chap] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
