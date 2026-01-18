from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ProductType:
    child1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class ExtendedProductType(ProductType):
    child2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Product(ExtendedProductType):
    class Meta:
        name = "product"
