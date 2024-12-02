from dataclasses import dataclass, field
from typing import ForwardRef, Union

__NAMESPACE__ = "foo"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    choice: list[
        Union[
            "Root.SkipAny",
            "Root.LaxAny",
            "Root.StrictAny",
            "Root.SkipOther",
            "Root.LaxLocal",
            "Root.StrictTarget",
            "Root.SkipBar",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "skipAny",
                    "type": ForwardRef("Root.SkipAny"),
                },
                {
                    "name": "laxAny",
                    "type": ForwardRef("Root.LaxAny"),
                },
                {
                    "name": "strictAny",
                    "type": ForwardRef("Root.StrictAny"),
                },
                {
                    "name": "skipOther",
                    "type": ForwardRef("Root.SkipOther"),
                },
                {
                    "name": "laxLocal",
                    "type": ForwardRef("Root.LaxLocal"),
                },
                {
                    "name": "strictTarget",
                    "type": ForwardRef("Root.StrictTarget"),
                },
                {
                    "name": "skipBar",
                    "type": ForwardRef("Root.SkipBar"),
                },
            ),
        },
    )

    @dataclass
    class SkipAny:
        any_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "process_contents": "skip",
            },
        )

    @dataclass
    class LaxAny:
        any_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )

    @dataclass
    class StrictAny:
        any_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )

    @dataclass
    class SkipOther:
        other_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
                "process_contents": "skip",
            },
        )

    @dataclass
    class LaxLocal:
        local_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##local",
            },
        )

    @dataclass
    class StrictTarget:
        target_namespace_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##targetNamespace",
            },
        )

    @dataclass
    class SkipBar:
        bar_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "bar",
                "process_contents": "skip",
            },
        )
