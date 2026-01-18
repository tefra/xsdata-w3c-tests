from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod


@dataclass(kw_only=True)
class PublicationType:
    title: str = field(
        metadata={
            "name": "Title",
            "type": "Element",
            "required": True,
        }
    )
    author: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Author",
            "type": "Element",
        },
    )
    date: XmlPeriod = field(
        metadata={
            "name": "Date",
            "type": "Element",
            "required": True,
        }
    )
    kind: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Example:
    publication: list[PublicationType | Example.KindBook] = field(
        default_factory=list,
        metadata={
            "name": "Publication",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class KindBook(PublicationType):
        isbn: str = field(
            metadata={
                "name": "ISBN",
                "type": "Element",
                "required": True,
            }
        )
        publisher: str = field(
            metadata={
                "name": "Publisher",
                "type": "Element",
                "required": True,
            }
        )
