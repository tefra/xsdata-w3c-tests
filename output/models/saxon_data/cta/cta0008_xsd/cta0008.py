from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlPeriod


@dataclass
class PublicationType:
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "required": True,
        },
    )
    author: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Author",
            "type": "Element",
        },
    )
    date: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "required": True,
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Example:
    publication: list[Union[PublicationType, "Example.KindBook"]] = field(
        default_factory=list,
        metadata={
            "name": "Publication",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class KindBook(PublicationType):
        isbn: Optional[str] = field(
            default=None,
            metadata={
                "name": "ISBN",
                "type": "Element",
                "required": True,
            },
        )
        publisher: Optional[str] = field(
            default=None,
            metadata={
                "name": "Publisher",
                "type": "Element",
                "required": True,
            },
        )
