from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://xsdtesting"


class MySimpleType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | Doc.Elem = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
    class Elem:
        att: MySimpleType = field(
            init=False,
            default=MySimpleType.VALUE_1,
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
            },
        )
