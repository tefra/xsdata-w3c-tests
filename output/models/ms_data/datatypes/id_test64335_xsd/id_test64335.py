from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "urn:products"


@dataclass(kw_only=True)
class Product:
    price: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Apparel(Product):
    size: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    style: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MediaItem(Product):
    title: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    category: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Book(MediaItem):
    author: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    publish_date: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Cd(MediaItem):
    class Meta:
        name = "CD"

    artist: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    release_date: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Dvd(MediaItem):
    class Meta:
        name = "DVD"

    director: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    release_date: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ProductList:
    choice: list[Book | Dvd | Apparel | Cd] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "book",
                    "type": Book,
                    "namespace": "",
                },
                {
                    "name": "dvd",
                    "type": Dvd,
                    "namespace": "",
                },
                {
                    "name": "clothing",
                    "type": Apparel,
                    "namespace": "",
                },
                {
                    "name": "cd",
                    "type": Cd,
                    "namespace": "",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Products(ProductList):
    class Meta:
        name = "products"
        namespace = "urn:products"
