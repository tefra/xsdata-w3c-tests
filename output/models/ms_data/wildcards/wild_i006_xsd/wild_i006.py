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
            "required": True,
        }
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
                    "name": "a_element",
                    "wildcard": True,
                    "type": object,
                    "namespace": "a",
                },
                {
                    "name": "b_element",
                    "wildcard": True,
                    "type": object,
                    "namespace": "b",
                },
                {
                    "name": "targetNamespace_element",
                    "wildcard": True,
                    "type": object,
                    "namespace": "##targetNamespace",
                },
                {
                    "name": "local_element",
                    "wildcard": True,
                    "type": object,
                    "namespace": "##local",
                },
            ),
            "max_occurs": 10,
        }
    )
