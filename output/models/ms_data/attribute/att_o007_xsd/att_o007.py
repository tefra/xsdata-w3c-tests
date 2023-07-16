from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


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
        }
    )

    @dataclass
    class Elem:
        att: str = field(
            init=False,
            default="   1       2          3",
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
            }
        )
