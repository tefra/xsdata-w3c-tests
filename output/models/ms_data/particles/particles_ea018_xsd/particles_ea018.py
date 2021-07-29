from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a5: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
