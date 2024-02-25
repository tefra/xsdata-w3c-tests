from dataclasses import dataclass, field
from typing import List, Optional, Type

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
                    "type": Type["Root.A"],
                },
                {
                    "name": "B1",
                    "type": Type["Root.B1"],
                },
                {
                    "name": "B2",
                    "type": Type["Root.B2"],
                },
                {
                    "name": "B3",
                    "type": Type["Root.B3"],
                },
                {
                    "name": "B4",
                    "type": Type["Root.B4"],
                },
                {
                    "name": "B5",
                    "type": Type["Root.B5"],
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
