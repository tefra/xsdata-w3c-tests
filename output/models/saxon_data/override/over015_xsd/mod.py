from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class NotaFooBar(Enum):
    """
    :cvar FOO:
    :cvar BAR:
    :cvar BEZ:
    """
    FOO = "foo"
    BAR = "bar"
    BEZ = "bez"


@dataclass
class StructuredDate:
    """
    :ivar year:
    :ivar month:
    :ivar day:
    :ivar nota:
    """
    class Meta:
        name = "structuredDate"

    year: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    month: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    day: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    nota: Optional[NotaFooBar] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Doc:
    """
    :ivar para_or_bezzle:
    """
    class Meta:
        name = "doc"

    para_or_bezzle: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "para",
                    "type": StructuredDate,
                },
                {
                    "name": "bezzle",
                    "type": str,
                },
            ),
        }
    )
