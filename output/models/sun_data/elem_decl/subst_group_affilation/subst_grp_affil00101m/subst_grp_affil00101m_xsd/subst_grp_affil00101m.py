from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "ElemDecl/substGroupAffilation"


@dataclass
class PublicationType:
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
    date: Optional[XmlPeriod] = field(
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
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

    magazine: List[Magazine] = field(
        default_factory=list,
        metadata={
            "name": "Magazine",
            "type": "Element",
        }
    )
    book: List[Book] = field(
        default_factory=list,
        metadata={
            "name": "Book",
            "type": "Element",
        }
    )
    publication: List[Publication] = field(
        default_factory=list,
        metadata={
            "name": "Publication",
            "type": "Element",
        }
    )
