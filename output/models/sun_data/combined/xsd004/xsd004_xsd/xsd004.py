from dataclasses import dataclass, field
from typing import List, Type, Union

__NAMESPACE__ = "foo"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    choice: List[Union["Root.StrictTarget", "Root.LaxLocal", "Root.SkipAny", "Root.StrictAny", "Root.LaxAny", "Root.SkipOther", "Root.SkipBar"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "skipAny",
                    "type": Type["Root.SkipAny"],
                },
                {
                    "name": "laxAny",
                    "type": Type["Root.LaxAny"],
                },
                {
                    "name": "strictAny",
                    "type": Type["Root.StrictAny"],
                },
                {
                    "name": "skipOther",
                    "type": Type["Root.SkipOther"],
                },
                {
                    "name": "laxLocal",
                    "type": Type["Root.LaxLocal"],
                },
                {
                    "name": "strictTarget",
                    "type": Type["Root.StrictTarget"],
                },
                {
                    "name": "skipBar",
                    "type": Type["Root.SkipBar"],
                },
            ),
        }
    )

    @dataclass
    class SkipAny:
        any_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "process_contents": "skip",
            }
        )

    @dataclass
    class LaxAny:
        any_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )

    @dataclass
    class StrictAny:
        any_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )

    @dataclass
    class SkipOther:
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
                "process_contents": "skip",
            }
        )

    @dataclass
    class LaxLocal:
        local_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##local",
            }
        )

    @dataclass
    class StrictTarget:
        target_namespace_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##targetNamespace",
            }
        )

    @dataclass
    class SkipBar:
        bar_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "bar",
                "process_contents": "skip",
            }
        )
