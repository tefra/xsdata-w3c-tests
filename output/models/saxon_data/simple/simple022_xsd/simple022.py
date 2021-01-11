from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://simple022.ly/"


class PriceValue(Enum):
    VALUE_9_99 = Decimal("9.99")
    NA_N = Decimal("NaN")


@dataclass
class Price:
    class Meta:
        name = "price"
        namespace = "http://simple022.ly/"

    value: Optional[PriceValue] = field(
        default=None,
    )
