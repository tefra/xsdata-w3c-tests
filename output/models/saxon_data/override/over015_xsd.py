from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from xml.etree.ElementTree import QName


class NotaFooBar(Enum):
    FOO = QName("foo")
    BAR = QName("bar")
    BEZ = QName("bez")


@dataclass(kw_only=True)
class StructuredDate:
    class Meta:
        name = "structuredDate"

    year: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    month: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    day: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    nota: None | NotaFooBar = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    para_or_bezzle: list[StructuredDate | QName] = field(
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
