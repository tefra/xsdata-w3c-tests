from dataclasses import dataclass, field
from typing import List, Optional

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
        }
    )

    @dataclass
    class Elem:
        att: List[str] = field(
            init=False,
            default_factory=lambda: ["X", "Y", "Z"],
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
                "tokens": True,
            }
        )
