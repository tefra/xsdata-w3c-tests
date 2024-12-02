from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    a_or_b: list[Union["FooType.A", "FooType.B"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": ForwardRef("FooType.A"),
                    "namespace": "",
                },
                {
                    "name": "b",
                    "type": ForwardRef("FooType.B"),
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass
    class A:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class B:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )


@dataclass
class Doc(FooType):
    class Meta:
        name = "doc"
