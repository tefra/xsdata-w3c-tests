from dataclasses import dataclass, field
from typing import List, Optional


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
        metadata=dict(
            name="Title",
            type="Element",
            required=True
        )
    )
    author: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Author",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
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
    kind: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Example:
    """
    :ivar publication:
    """
    publication: List[PublicationType] = field(
        default_factory=list,
        metadata=dict(
            name="Publication",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )