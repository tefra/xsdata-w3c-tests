from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional

__NAMESPACE__ = "urn:test"


@dataclass
class Root:
    class Meta:
        namespace = "urn:test"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "A",
                    "type": ForwardRef("Root.A"),
                },
                {
                    "name": "B1",
                    "type": ForwardRef("Root.B1"),
                },
                {
                    "name": "B2",
                    "type": ForwardRef("Root.B2"),
                },
                {
                    "name": "B3",
                    "type": ForwardRef("Root.B3"),
                },
                {
                    "name": "B4",
                    "type": ForwardRef("Root.B4"),
                },
                {
                    "name": "B5",
                    "type": ForwardRef("Root.B5"),
                },
            ),
        },
    )

    @dataclass
    class A:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class B1:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class B2:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class B3:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class B4:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class B5:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
