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
        },
    )

    @dataclass
    class Elem:
        att: list[str] = field(
            init=False,
            default_factory=lambda: [
                "A",
                "B",
            ],
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
                "tokens": True,
            },
        )
