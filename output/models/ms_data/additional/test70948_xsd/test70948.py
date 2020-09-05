from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Confuse:
    """
    :ivar value:
    """
    class Meta:
        name = "confuse"

    value: Optional[Decimal] = field(
        default=None,
    )


@dataclass
class MyType:
    """
    :ivar value:
    """
    class Meta:
        name = "myType"

    value: Optional[int] = field(
        default=None,
    )


@dataclass
class Root(MyType):
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"
