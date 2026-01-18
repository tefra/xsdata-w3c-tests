from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Confuse:
    class Meta:
        name = "confuse"

    value: Decimal = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MyType(Confuse):
    class Meta:
        name = "myType"


@dataclass(kw_only=True)
class Root(MyType):
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"
