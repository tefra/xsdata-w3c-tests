from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "ElemDecl/substGroupAffilation"


@dataclass(kw_only=True)
class PublicationType:
    title: str = field(
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "ElemDecl/substGroupAffilation",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Article(PublicationType):
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"


@dataclass(kw_only=True)
class BookType(PublicationType):
    author: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "ElemDecl/substGroupAffilation",
        },
    )


@dataclass(kw_only=True)
class MagazineType(PublicationType):
    date: XmlPeriod = field(
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "ElemDecl/substGroupAffilation",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Publication(PublicationType):
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"


@dataclass(kw_only=True)
class Book(BookType):
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"


@dataclass(kw_only=True)
class Magazine(MagazineType):
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"


@dataclass(kw_only=True)
class BookStore:
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

    magazine_or_book: list[Magazine | Book] = field(
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
