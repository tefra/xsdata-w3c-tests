from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "foo"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class C:
    class Meta:
        name = "c"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    mixed_or_element_only: list[Union["Root.Mixed", "Root.ElementOnly"]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "mixed",
                        "type": ForwardRef("Root.Mixed"),
                    },
                    {
                        "name": "elementOnly",
                        "type": ForwardRef("Root.ElementOnly"),
                    },
                ),
            },
        )
    )

    @dataclass
    class Mixed:
        content: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
                "choices": (
                    {
                        "name": "a",
                        "type": A,
                    },
                    {
                        "name": "b",
                        "type": B,
                    },
                    {
                        "name": "c",
                        "type": C,
                    },
                ),
            },
        )

    @dataclass
    class ElementOnly:
        a_or_b_or_c: list[Union[A, B, C]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "a",
                        "type": A,
                    },
                    {
                        "name": "b",
                        "type": B,
                    },
                    {
                        "name": "c",
                        "type": C,
                    },
                ),
            },
        )
