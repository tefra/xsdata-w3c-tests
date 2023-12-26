from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Bar:
    class Meta:
        name = "bar"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "a",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "b",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##targetNamespace",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##local",
                },
            ),
            "max_occurs": 10,
        },
    )
