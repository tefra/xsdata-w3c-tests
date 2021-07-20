from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/1999/xhtml"


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "http://www.w3.org/1999/xhtml"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://www.w3.org/1999/xhtml"

    target_namespace_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
            "required": True,
        }
    )
