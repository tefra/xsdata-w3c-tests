from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Test:
    class Meta:
        name = "test"

    a_or_b: Optional[Union["Test.A", "Test.B"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": ForwardRef("Test.A"),
                    "namespace": "",
                },
                {
                    "name": "b",
                    "type": ForwardRef("Test.B"),
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
class Root(Test):
    class Meta:
        name = "root"
