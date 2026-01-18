from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    choice: list[
        Root.SkipAny
        | Root.LaxAny
        | Root.StrictAny
        | Root.SkipOther
        | Root.LaxLocal
        | Root.StrictTarget
        | Root.SkipBar
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

    @dataclass(kw_only=True)
    class SkipAny:
        any_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "process_contents": "skip",
            },
        )

    @dataclass(kw_only=True)
    class LaxAny:
        any_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class StrictAny:
        any_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class SkipOther:
        other_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
                "process_contents": "skip",
            },
        )

    @dataclass(kw_only=True)
    class LaxLocal:
        local_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##local",
            },
        )

    @dataclass(kw_only=True)
    class StrictTarget:
        target_namespace_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##targetNamespace",
            },
        )

    @dataclass(kw_only=True)
    class SkipBar:
        bar_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "bar",
                "process_contents": "skip",
            },
        )
