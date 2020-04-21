from dataclasses import dataclass, field
from lxml.etree import QName
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
        metadata=dict(
            name="skipAny",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    lax_any: List["Root.LaxAny"] = field(
        default_factory=list,
        metadata=dict(
            name="laxAny",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strict_any: List["Root.StrictAny"] = field(
        default_factory=list,
        metadata=dict(
            name="strictAny",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    skip_other: List["Root.SkipOther"] = field(
        default_factory=list,
        metadata=dict(
            name="skipOther",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    lax_local: List["Root.LaxLocal"] = field(
        default_factory=list,
        metadata=dict(
            name="laxLocal",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strict_local: List["Root.StrictLocal"] = field(
        default_factory=list,
        metadata=dict(
            name="strictLocal",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    strict_target: List["Root.StrictTarget"] = field(
        default_factory=list,
        metadata=dict(
            name="strictTarget",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    skip_bar: List["Root.SkipBar"] = field(
        default_factory=list,
        metadata=dict(
            name="skipBar",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class SkipAny:
        """
        :ivar any_attributes:
        """
        any_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##any"
            )
        )

    @dataclass
    class LaxAny:
        """
        :ivar any_attributes:
        """
        any_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##any"
            )
        )

    @dataclass
    class StrictAny:
        """
        :ivar any_attributes:
        """
        any_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##any"
            )
        )

    @dataclass
    class SkipOther:
        """
        :ivar other_attributes:
        """
        other_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##other"
            )
        )

    @dataclass
    class LaxLocal:
        """
        :ivar local_attributes:
        """
        local_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##local"
            )
        )

    @dataclass
    class StrictLocal:
        """
        :ivar local_attributes:
        """
        local_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##local"
            )
        )

    @dataclass
    class StrictTarget:
        """
        :ivar target_namespace_attributes:
        """
        target_namespace_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##targetNamespace"
            )
        )

    @dataclass
    class SkipBar:
        """
        :ivar bar_attributes:
        """
        bar_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="bar"
            )
        )
