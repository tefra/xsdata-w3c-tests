from dataclasses import dataclass, field
from typing import Any, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    target_namespace_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
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
        },
    )


@dataclass
class R(B):
    target_namespace_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
