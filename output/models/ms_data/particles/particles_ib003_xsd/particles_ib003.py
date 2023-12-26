from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Bar:
    class Meta:
        name = "bar"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Base:
    class Meta:
        name = "base"

    foo_or_bar: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "bar",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 6,
        },
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"

    foo_or_bar: List[Union[Foo, Bar]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": Foo,
                },
                {
                    "name": "bar",
                    "type": Bar,
                },
            ),
            "max_occurs": 3,
        },
    )
