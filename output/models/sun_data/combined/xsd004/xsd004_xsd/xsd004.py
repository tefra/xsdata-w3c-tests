from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "foo"


@dataclass
class Root:
    """
    :ivar skip_any:
    :ivar lax_any:
    :ivar strict_any:
    :ivar skip_other:
    :ivar lax_local:
    :ivar strict_target:
    :ivar skip_bar:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    skip_any: List["Root.SkipAny"] = field(
        default_factory=list,
        metadata={
            "name": "skipAny",
            "type": "Element",
        }
    )
    lax_any: List["Root.LaxAny"] = field(
        default_factory=list,
        metadata={
            "name": "laxAny",
            "type": "Element",
        }
    )
    strict_any: List["Root.StrictAny"] = field(
        default_factory=list,
        metadata={
            "name": "strictAny",
            "type": "Element",
        }
    )
    skip_other: List["Root.SkipOther"] = field(
        default_factory=list,
        metadata={
            "name": "skipOther",
            "type": "Element",
        }
    )
    lax_local: List["Root.LaxLocal"] = field(
        default_factory=list,
        metadata={
            "name": "laxLocal",
            "type": "Element",
        }
    )
    strict_target: List["Root.StrictTarget"] = field(
        default_factory=list,
        metadata={
            "name": "strictTarget",
            "type": "Element",
        }
    )
    skip_bar: List["Root.SkipBar"] = field(
        default_factory=list,
        metadata={
            "name": "skipBar",
            "type": "Element",
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
