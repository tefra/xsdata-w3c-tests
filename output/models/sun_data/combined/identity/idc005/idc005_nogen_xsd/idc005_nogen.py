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
        metadata=dict(
            name="Book",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
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
            metadata=dict(
                name="Title",
                type="Element",
                required=True
            )
        )
        author: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Author",
                type="Element",
                required=True
            )
        )
        date: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Date",
                type="Element",
                required=True
            )
        )
        isbn: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ISBN",
                type="Element"
            )
        )
        publisher: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Publisher",
                type="Element",
                required=True
            )
        )
