from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


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

    foo_or_bar: list[Union["Base.Foo", "Base.Bar"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": ForwardRef("Base.Foo"),
                    "namespace": "",
                    "max_occurs": 6,
                },
                {
                    "name": "bar",
                    "type": ForwardRef("Base.Bar"),
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

    foo_or_bar: list[Union[Foo, Bar]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": Foo,
                    "max_occurs": 3,
                },
                {
                    "name": "bar",
                    "type": Bar,
                },
            ),
            "max_occurs": 3,
        },
    )
