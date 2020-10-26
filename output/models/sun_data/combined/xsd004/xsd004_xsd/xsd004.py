from dataclasses import dataclass, field
from typing import List, Type

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
        :ivar any_element:
        """
        any_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "min_occurs": 1,
            }
        )

    @dataclass
    class LaxAny:
        """
        :ivar any_element:
        """
        any_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "min_occurs": 1,
            }
        )

    @dataclass
    class StrictAny:
        """
        :ivar any_element:
        """
        any_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "min_occurs": 1,
            }
        )

    @dataclass
    class SkipOther:
        """
        :ivar other_element:
        """
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
                "min_occurs": 1,
            }
        )

    @dataclass
    class LaxLocal:
        """
        :ivar local_element:
        """
        local_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##local",
                "min_occurs": 1,
            }
        )

    @dataclass
    class StrictTarget:
        """
        :ivar target_namespace_element:
        """
        target_namespace_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##targetNamespace",
                "min_occurs": 1,
            }
        )

    @dataclass
    class SkipBar:
        """
        :ivar bar_element:
        """
        bar_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "bar",
                "min_occurs": 1,
            }
        )
