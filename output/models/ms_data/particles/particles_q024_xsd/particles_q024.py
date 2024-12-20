from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
            "max_occurs": 4,
        },
    )


@dataclass
class R:
    foo: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo: list[object] = field(
        default_factory=list,
        metadata={
            "wrapper": "elem",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
