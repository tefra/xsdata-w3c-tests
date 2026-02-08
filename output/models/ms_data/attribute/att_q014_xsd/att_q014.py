from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class InternationalPrice:
    class Meta:
        name = "internationalPrice"
        namespace = "http://xsdtesting"

    value: Decimal = field()
    currency: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    international_price: InternationalPrice = field(
        metadata={
            "name": "internationalPrice",
            "type": "Element",
        }
    )
