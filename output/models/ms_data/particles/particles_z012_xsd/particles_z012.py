from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class E2:
    class Meta:
        namespace = "http://xsdtesting"

    value: int = field()


class MyType10Value(Enum):
    X = "x"
    Y = "y"


@dataclass(kw_only=True)
class Ct1:
    class Meta:
        name = "CT1"

    att1: None | bool | float | int | MyType10Value = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )


@dataclass(kw_only=True)
class E1:
    class Meta:
        namespace = "http://xsdtesting"

    value: bool | float | int | MyType10Value = field()


@dataclass(kw_only=True)
class Ct2(Ct1):
    class Meta:
        name = "CT2"


@dataclass(kw_only=True)
class E3(Ct2):
    class Meta:
        namespace = "http://xsdtesting"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    e2_or_e1_or_e3: list[E2 | E1 | E3] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "E2",
                    "type": E2,
                },
                {
                    "name": "E1",
                    "type": E1,
                },
                {
                    "name": "E3",
                    "type": E3,
                },
            ),
        },
    )
