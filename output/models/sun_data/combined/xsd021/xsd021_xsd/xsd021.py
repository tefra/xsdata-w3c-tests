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
            "Root.StrictLocal",
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
                    "name": "strictLocal",
                    "type": ForwardRef("Root.StrictLocal"),
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
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass
    class LaxAny:
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass
    class StrictAny:
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass
    class SkipOther:
        other_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            },
        )

    @dataclass
    class LaxLocal:
        local_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##local",
            },
        )

    @dataclass
    class StrictLocal:
        local_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##local",
            },
        )

    @dataclass
    class StrictTarget:
        target_namespace_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##targetNamespace",
            },
        )

    @dataclass
    class SkipBar:
        bar_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "bar",
            },
        )
