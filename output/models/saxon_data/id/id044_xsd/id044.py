from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Type, Union

__NAMESPACE__ = "http://id044.ly/"


@dataclass
class Chap:
    class Meta:
        name = "chap"

    section: List["Chap.Section"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://id044.ly/",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Section:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        nr: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        ref: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://id044.ly/"

    chap_or_appx: List[Union["Doc.Chap", "Doc.Appx"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "chap",
                    "type": Type["Doc.Chap"],
                },
                {
                    "name": "appx",
                    "type": Type["Doc.Appx"],
                },
            ),
        },
    )

    @dataclass
    class Chap(Chap):
        pass

    @dataclass
    class Appx(Chap):
        pass
