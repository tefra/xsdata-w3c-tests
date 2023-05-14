from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Chap:
    class Meta:
        name = "chap"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    de: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lang: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fr: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Part:
    class Meta:
        name = "part"

    chap: List[Chap] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    lang: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    part: List[Part] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    lang: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
