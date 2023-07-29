from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://foobar"


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    target_namespace_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
            "process_contents": "skip",
        }
    )
