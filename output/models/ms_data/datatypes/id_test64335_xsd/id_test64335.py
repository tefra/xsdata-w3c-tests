from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:products"


@dataclass
class Apparel:
    """
    :ivar price:
    :ivar description:
    :ivar id:
    :ivar size:
    :ivar style:
    """
    price: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    size: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    style: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Book:
    """
    :ivar price:
    :ivar description:
    :ivar id:
    :ivar title:
    :ivar category:
    :ivar author:
    :ivar publish_date:
    """
    price: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    category: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    author: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    publish_date: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Cd:
    """
    :ivar price:
    :ivar description:
    :ivar id:
    :ivar title:
    :ivar category:
    :ivar artist:
    :ivar release_date:
    """
    class Meta:
        name = "CD"

    price: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    category: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    artist: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    release_date: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Dvd:
    """
    :ivar price:
    :ivar description:
    :ivar id:
    :ivar title:
    :ivar category:
    :ivar director:
    :ivar release_date:
    """
    class Meta:
        name = "DVD"

    price: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    category: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    director: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    release_date: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class ProductList:
    """
    :ivar book:
    :ivar dvd:
    :ivar clothing:
    :ivar cd:
    """
    book: List[Book] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    dvd: List[Dvd] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    clothing: List[Apparel] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    cd: List[Cd] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Products(ProductList):
    class Meta:
        name = "products"
        namespace = "urn:products"
