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

    other_element_or_target_namespace_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "other_element",
                    "wildcard": True,
                    "type": object,
                    "namespace": "##other",
                },
                {
                    "name": "targetNamespace_element",
                    "wildcard": True,
                    "type": object,
                    "namespace": "##targetNamespace",
                },
            ),
            "max_occurs": 10,
        }
    )
