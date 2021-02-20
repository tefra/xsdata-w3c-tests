from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class InternationalPrice:
    class Meta:
        name = "internationalPrice"
        namespace = "http://xsdtesting"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    international_price: Optional[InternationalPrice] = field(
        default=None,
        metadata={
            "name": "internationalPrice",
            "type": "Element",
            "required": True,
        }
    )
