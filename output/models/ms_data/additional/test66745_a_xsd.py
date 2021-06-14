from dataclasses import dataclass, field
from typing import List, Optional, Type


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Foo1(Foo):
    class Meta:
        name = "foo1"
        namespace = "foo1"

    x: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Bar:
    class Meta:
        name = "bar"
        namespace = "foo"

    foo1_or_foo_or_bar: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo1",
                    "type": Foo1,
                    "namespace": "foo1",
                },
                {
                    "name": "foo",
                    "type": Foo,
                },
                {
                    "name": "bar",
                    "type": Type["Bar"],
                },
            ),
        }
    )
