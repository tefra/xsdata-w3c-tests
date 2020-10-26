from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "urn:products"


@dataclass
class Product:
    """
    :ivar price:
    :ivar description:
    :ivar id:
    """
    price: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Apparel(Product):
    """
    :ivar size:
    :ivar style:
    """
    size: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class MediaItem(Product):
    """
    :ivar title:
    :ivar category:
    """
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Book(MediaItem):
    """
    :ivar author:
    :ivar publish_date:
    """
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    publish_date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Cd(MediaItem):
    """
    :ivar artist:
    :ivar release_date:
    """
    class Meta:
        name = "CD"

    artist: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    release_date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Dvd(MediaItem):
    """
    :ivar director:
    :ivar release_date:
    """
    class Meta:
        name = "DVD"

    director: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    release_date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ProductList:
    """
    :ivar choice:
    """
    choice: List[object] = field(
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
        }
    )


@dataclass
class Products(ProductList):
    class Meta:
        name = "products"
        namespace = "urn:products"
