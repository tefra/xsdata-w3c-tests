from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://simple022.ly/"


@dataclass
class Price:
    """
    :ivar value:
    """
    class Meta:
        name = "price"
        namespace = "http://simple022.ly/"

    value: Optional["Price.Value"] = field(
        default=None,
    )

    class Value(Enum):
        """
        :cvar VALUE_9_99:
        :cvar NA_N:
        """
        VALUE_9_99 = Decimal('9.99')
        NA_N = Decimal('NaN')
