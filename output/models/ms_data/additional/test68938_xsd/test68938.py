from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar value:
    """
    class Meta:
        name = "foo"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            total_digits=5,
            fraction_digits=2
        )
    )