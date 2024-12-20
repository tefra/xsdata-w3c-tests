from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.books.org"


@dataclass
class BookStore:
    class Meta:
        namespace = "http://www.books.org"

    book: list["BookStore.Book"] = field(
        default_factory=list,
        metadata={
            "name": "Book",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Book:
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
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
