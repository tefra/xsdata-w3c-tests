from dataclasses import dataclass, field
from typing import Dict, List, Type

__NAMESPACE__ = "foo"


@dataclass
class Root:
    """
    :ivar choice:
    """
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
        """
        :ivar any_attributes:
        """
        any_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            }
        )

    @dataclass
    class LaxAny:
        """
        :ivar any_attributes:
        """
        any_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            }
        )

    @dataclass
    class StrictAny:
        """
        :ivar any_attributes:
        """
        any_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            }
        )

    @dataclass
    class SkipOther:
        """
        :ivar other_attributes:
        """
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class LaxLocal:
        """
        :ivar local_attributes:
        """
        local_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##local",
            }
        )

    @dataclass
    class StrictLocal:
        """
        :ivar local_attributes:
        """
        local_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##local",
            }
        )

    @dataclass
    class StrictTarget:
        """
        :ivar target_namespace_attributes:
        """
        target_namespace_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##targetNamespace",
            }
        )

    @dataclass
    class SkipBar:
        """
        :ivar bar_attributes:
        """
        bar_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "bar",
            }
        )
