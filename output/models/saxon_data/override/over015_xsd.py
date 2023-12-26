from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from xml.etree.ElementTree import QName


class NotaFooBar(Enum):
    FOO = QName("foo")
    BAR = QName("bar")
    BEZ = QName("bez")


@dataclass
class StructuredDate:
    class Meta:
        name = "structuredDate"

    year: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    month: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    day: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    nota: Optional[NotaFooBar] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    para_or_bezzle: List[Union[StructuredDate, QName]] = field(
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
                    "type": QName,
                },
            ),
        },
    )
