from dataclasses import dataclass, field
from typing import Dict, List, Type

__NAMESPACE__ = "foo"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    choice: List[object] = field(
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
                    "name": "strictLocal",
                    "type": Type["Root.StrictLocal"],
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
        any_attributes: Dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            }
        )

    @dataclass
    class LaxAny:
        any_attributes: Dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            }
        )

    @dataclass
    class StrictAny:
        any_attributes: Dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            }
        )

    @dataclass
    class SkipOther:
        other_attributes: Dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class LaxLocal:
        local_attributes: Dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##local",
            }
        )

    @dataclass
    class StrictLocal:
        local_attributes: Dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##local",
            }
        )

    @dataclass
    class StrictTarget:
        target_namespace_attributes: Dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##targetNamespace",
            }
        )

    @dataclass
    class SkipBar:
        bar_attributes: Dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "bar",
            }
        )
