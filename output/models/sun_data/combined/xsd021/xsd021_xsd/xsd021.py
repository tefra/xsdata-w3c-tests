from dataclasses import dataclass, field
from typing import Dict, List

__NAMESPACE__ = "foo"


@dataclass
class Root:
    """
    :ivar skip_any:
    :ivar lax_any:
    :ivar strict_any:
    :ivar skip_other:
    :ivar lax_local:
    :ivar strict_local:
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
    strict_local: List["Root.StrictLocal"] = field(
        default_factory=list,
        metadata={
            "name": "strictLocal",
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
