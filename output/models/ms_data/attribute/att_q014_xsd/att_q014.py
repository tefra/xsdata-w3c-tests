from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class InternationalPrice:
    """
    :ivar value:
    :ivar currency:
    """
    class Meta:
        name = "internationalPrice"
        namespace = "http://xsdtesting"

    value: Optional[Decimal] = field(
        default=None,
    )
    currency: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )


@dataclass
class Doc:
    """
    :ivar international_price:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    international_price: Optional[InternationalPrice] = field(
        default=None,
        metadata=dict(
            name="internationalPrice",
            type="Element",
            required=True
        )
    )
