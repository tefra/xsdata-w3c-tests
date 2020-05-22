from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/substGroupAffilation"


@dataclass
class PublicationType:
    """
    :ivar title:
    """
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Title",
            type="Element",
            namespace="ElemDecl/substGroupAffilation",
            required=True
        )
    )


@dataclass
class Article(PublicationType):
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"


@dataclass
class BookType(PublicationType):
    """
    :ivar author:
    """
    author: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Author",
            type="Element",
            namespace="ElemDecl/substGroupAffilation",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class MagazineType(PublicationType):
    """
    :ivar date:
    """
    date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Date",
            type="Element",
            namespace="ElemDecl/substGroupAffilation",
            required=True
        )
    )


@dataclass
class Book(BookType):
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"


@dataclass
class Magazine(MagazineType):
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"


@dataclass
class BookStore:
    """
    :ivar magazine:
    :ivar book:
    :ivar publication:
    """
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

    magazine: List[Magazine] = field(
        default_factory=list,
        metadata=dict(
            name="Magazine",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    book: List[Book] = field(
        default_factory=list,
        metadata=dict(
            name="Book",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    publication: List[PublicationType] = field(
        default_factory=list,
        metadata=dict(
            name="Publication",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
