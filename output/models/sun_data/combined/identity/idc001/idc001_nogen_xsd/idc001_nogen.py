from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.publishing.org"


@dataclass
class BookCatalogue:
    """
    :ivar book:
    """
    class Meta:
        namespace = "http://www.publishing.org"

    book: List["BookCatalogue.Book"] = field(
        default_factory=list,
        metadata={
            "name": "Book",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Book:
        """
        :ivar title:
        :ivar author:
        :ivar date:
        :ivar isbn:
        :ivar publisher:
        """
        title: Optional[str] = field(
            default=None,
            metadata={
                "name": "Title",
                "type": "Element",
                "required": True,
            }
        )
        author: Optional[str] = field(
            default=None,
            metadata={
                "name": "Author",
                "type": "Element",
                "required": True,
            }
        )
        date: Optional[str] = field(
            default=None,
            metadata={
                "name": "Date",
                "type": "Element",
                "required": True,
            }
        )
        isbn: Optional[str] = field(
            default=None,
            metadata={
                "name": "ISBN",
                "type": "Element",
            }
        )
        publisher: Optional[str] = field(
            default=None,
            metadata={
                "name": "Publisher",
                "type": "Element",
                "required": True,
            }
        )
