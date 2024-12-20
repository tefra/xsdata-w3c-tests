from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


class MySimpleType(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional["Doc.Elem"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Elem:
        att: MySimpleType = field(
            init=False,
            default=MySimpleType.VALUE_1,
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
            },
        )
