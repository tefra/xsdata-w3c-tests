from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Any:
    class Meta:
        name = "any"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 100,
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: List[Any] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 100,
        }
    )


@dataclass
class Foo(Any):
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"
