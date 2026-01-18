from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.publishing.org"


@dataclass(kw_only=True)
class BookCatalogue:
    class Meta:
        namespace = "http://www.publishing.org"

    book: list[BookCatalogue.Book] = field(
        default_factory=list,
        metadata={
            "name": "Book",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Book:
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
        isbn: None | str = field(
            default=None,
            metadata={
                "name": "ISBN",
                "type": "Element",
            },
        )
        publisher: str = field(
            metadata={
                "name": "Publisher",
                "type": "Element",
                "required": True,
            }
        )
