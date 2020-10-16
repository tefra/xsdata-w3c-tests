from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProductType:
    """
    :ivar child1:
    """
    child1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ExtendedProductType(ProductType):
    """
    :ivar child2:
    """
    child2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Product(ExtendedProductType):
    class Meta:
        name = "product"
