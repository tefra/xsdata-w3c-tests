from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class PublicationType:
    """
    :ivar title:
    :ivar author:
    :ivar date:
    :ivar kind:
    """
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "required": True,
        }
    )
    author: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Author",
            "type": "Element",
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
    kind: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Example:
    """
    :ivar publication:
    """
    publication: List[Union[PublicationType, "Example.KindBook"]] = field(
        default_factory=list,
        metadata={
            "name": "Publication",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class KindBook(PublicationType):
        """
        :ivar isbn:
        :ivar publisher:
        """
        isbn: Optional[str] = field(
            default=None,
            metadata={
                "name": "ISBN",
                "type": "Element",
                "required": True,
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
