from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://simple003.ly/"


@dataclass
class Chap:
    class Meta:
        name = "chap"

    section: List["Chap.Section"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple003.ly/",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Section:
        value: str = field(
            default="",
            metadata={
                "required": True,
            }
        )
        nr: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        ref: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://simple003.ly/"

    chap_or_appx: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "chap",
                    "type": Chap,
                },
                {
                    "name": "appx",
                    "type": Chap,
                },
            ),
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2012.*",
        }
    )
