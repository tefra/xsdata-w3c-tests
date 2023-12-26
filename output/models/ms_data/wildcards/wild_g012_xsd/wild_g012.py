from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://foobar"


@dataclass
class Bar:
    class Meta:
        name = "bar"
        namespace = "http://foobar"

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
        namespace = "http://foobar"

    target_namespace_w3_org_1999_xhtml_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace http://www.w3.org/1999/xhtml",
        },
    )
