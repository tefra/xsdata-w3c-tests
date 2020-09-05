from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional


@dataclass
class FooType:
    """
    :ivar foo:
    """
    class Meta:
        name = "fooType"

    foo: Optional["FooType.Foo"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )

    class Foo(Enum):
        """
        :cvar VALUE_1_1:
        """
        VALUE_1_1 = Decimal('1.1')


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
