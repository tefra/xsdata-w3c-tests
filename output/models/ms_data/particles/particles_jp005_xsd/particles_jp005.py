from dataclasses import dataclass, field
from typing import Any, List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    target_namespace_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
            "max_occurs": 10,
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
    foo: List[Foo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "min_occurs": 1,
            "max_occurs": 10,
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
