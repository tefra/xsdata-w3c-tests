from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.books.org"


@dataclass(kw_only=True)
class BookStore:
    class Meta:
        namespace = "http://www.books.org"

    book: list[BookStore.Book] = field(
        default_factory=list,
        metadata={
            "name": "Book",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Book:
        id: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        title: str = field(
            metadata={
                "name": "Title",
                "type": "Element",
                "required": True,
            }
        )
        author: str = field(
            metadata={
                "name": "Author",
                "type": "Element",
                "required": True,
            }
        )
        date: str = field(
            metadata={
                "name": "Date",
                "type": "Element",
                "required": True,
            }
        )
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
