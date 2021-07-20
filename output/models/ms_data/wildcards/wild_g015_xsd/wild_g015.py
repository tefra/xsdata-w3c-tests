from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://foobar"


@dataclass
class Bar:
    class Meta:
        name = "bar"
        namespace = "http://foobar"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
