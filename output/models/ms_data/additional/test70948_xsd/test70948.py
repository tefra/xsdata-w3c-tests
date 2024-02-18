from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Confuse:
    class Meta:
        name = "confuse"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class MyType(Confuse):
    class Meta:
        name = "myType"


@dataclass
class Root(MyType):
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"
