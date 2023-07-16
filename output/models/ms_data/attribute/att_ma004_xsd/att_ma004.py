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
    ga1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )

    @dataclass
    class Elem:
        ga1: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
            }
        )
        ga2: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://xsdtesting",
            }
        )
