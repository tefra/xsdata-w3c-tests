from dataclasses import dataclass, field
from typing import List, Optional, Type, Union


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    a_or_b: List[Union["FooType.A", "FooType.B"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": Type["FooType.A"],
                    "namespace": "",
                },
                {
                    "name": "b",
                    "type": Type["FooType.B"],
                    "namespace": "",
                },
            ),
            "min_occurs": 2,
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
