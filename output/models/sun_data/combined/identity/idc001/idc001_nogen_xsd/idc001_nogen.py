from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.publishing.org"


@dataclass
class BookCatalogue:
    class Meta:
        namespace = "http://www.publishing.org"

    book: list["BookCatalogue.Book"] = field(
        default_factory=list,
        metadata={
            "name": "Book",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Book:
        title: Optional[str] = field(
            default=None,
            metadata={
                "name": "Title",
                "type": "Element",
                "required": True,
            },
        )
        author: Optional[str] = field(
            default=None,
            metadata={
                "name": "Author",
                "type": "Element",
                "required": True,
            },
        )
        date: Optional[str] = field(
            default=None,
            metadata={
                "name": "Date",
                "type": "Element",
                "required": True,
            },
        )
        isbn: Optional[str] = field(
            default=None,
            metadata={
                "name": "ISBN",
                "type": "Element",
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
