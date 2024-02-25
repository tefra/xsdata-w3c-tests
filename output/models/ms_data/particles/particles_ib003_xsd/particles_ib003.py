from dataclasses import dataclass, field
from typing import List, Optional, Type, Union


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

    foo_or_bar: List[Union["Base.Foo", "Base.Bar"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": Type["Base.Foo"],
                    "namespace": "",
                },
                {
                    "name": "bar",
                    "type": Type["Base.Bar"],
                    "namespace": "",
                },
            ),
            "max_occurs": 6,
        },
    )

    @dataclass
    class Foo:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Bar:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
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
