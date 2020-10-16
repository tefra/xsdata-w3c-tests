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
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "ElemDecl/substGroupAffilation",
            "required": True,
        }
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
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "ElemDecl/substGroupAffilation",
        }
    )


@dataclass
class MagazineType(PublicationType):
    """
    :ivar date:
    """
    date: Optional[str] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "ElemDecl/substGroupAffilation",
            "required": True,
        }
    )


@dataclass
class Publication(PublicationType):
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"


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
        metadata={
            "name": "Magazine",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    book: List[Book] = field(
        default_factory=list,
        metadata={
            "name": "Book",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    publication: List[Publication] = field(
        default_factory=list,
        metadata={
            "name": "Publication",
            "type": "Element",
            "min_occurs": 1,
        }
    )
