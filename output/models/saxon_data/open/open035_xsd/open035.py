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
            }
        )
        title: str = field(
            metadata={
                "name": "Title",
                "type": "Element",
            }
        )
        author: str = field(
            metadata={
                "name": "Author",
                "type": "Element",
            }
        )
        date: str = field(
            metadata={
                "name": "Date",
                "type": "Element",
            }
        )
        isbn: str = field(
            metadata={
                "name": "ISBN",
                "type": "Element",
            }
        )
        publisher: str = field(
            metadata={
                "name": "Publisher",
                "type": "Element",
            }
        )
