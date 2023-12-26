from dataclasses import dataclass, field
from typing import List, Optional, Union
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
        },
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
        },
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
        },
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
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

    magazine_or_book: List[Union[Magazine, Book]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Magazine",
                    "type": Magazine,
                },
                {
                    "name": "Book",
                    "type": Book,
                },
            ),
        },
    )
