from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class FooType:
    """
    :ivar foo:
    """
    class Meta:
        name = "fooType"

    foo: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            min_inclusive=1.1
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
