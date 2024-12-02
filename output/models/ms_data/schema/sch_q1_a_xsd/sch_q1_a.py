from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "ns-a"


@dataclass
class BCt:
    class Meta:
        name = "b-ct"

    b1_or_b2: Optional[Union["BCt.B1", "BCt.B2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b1",
                    "type": ForwardRef("BCt.B1"),
                    "namespace": "ns-a",
                },
                {
                    "name": "b2",
                    "type": ForwardRef("BCt.B2"),
                    "namespace": "ns-a",
                },
            ),
        },
    )
    b3_or_b4: Optional[Union["BCt.B3", "BCt.B4"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b3",
                    "type": ForwardRef("BCt.B3"),
                    "namespace": "ns-a",
                },
                {
                    "name": "b4",
                    "type": ForwardRef("BCt.B4"),
                    "namespace": "ns-a",
                },
            ),
        },
    )

    @dataclass
    class B1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "ns-a",
                "required": True,
            },
        )

    @dataclass
    class B2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "ns-a",
                "required": True,
            },
        )

    @dataclass
    class B3:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "ns-a",
                "required": True,
            },
        )

    @dataclass
    class B4:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "ns-a",
                "required": True,
            },
        )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class E1(BCt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
