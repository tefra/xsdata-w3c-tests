from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "urn:products"


@dataclass
class Product:
    price: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Apparel(Product):
    size: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class MediaItem(Product):
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Book(MediaItem):
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    publish_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Cd(MediaItem):
    class Meta:
        name = "CD"

    artist: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    release_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Dvd(MediaItem):
    class Meta:
        name = "DVD"

    director: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    release_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class ProductList:
    choice: List[Union[Book, Dvd, Apparel, Cd]] = field(
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


@dataclass
class Products(ProductList):
    class Meta:
        name = "products"
        namespace = "urn:products"
