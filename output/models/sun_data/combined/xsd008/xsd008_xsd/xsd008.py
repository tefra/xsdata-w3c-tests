from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class Facet:
    """
    :ivar annotation:
    :ivar value:
    """
    class Meta:
        name = "facet"
        namespace = "foo"

    annotation: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class IntType:
    """
    :ivar annotation:
    :ivar value:
    """
    class Meta:
        name = "int"
        namespace = "foo"

    annotation: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class LongType:
    """
    :ivar annotation:
    :ivar value:
    """
    class Meta:
        name = "longType"

    annotation: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="foo"
        )
    )
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class YesNo:
    """
    :ivar annotation:
    :ivar value:
    """
    class Meta:
        name = "yesNo"
        namespace = "foo"

    annotation: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class Long(LongType):
    class Meta:
        name = "long"
        namespace = "foo"


@dataclass
class Generic:
    """
    :ivar int_value:
    :ivar long:
    :ivar yes_no:
    :ivar facet:
    """
    class Meta:
        name = "generic"
        namespace = "foo"

    int_value: List[IntType] = field(
        default_factory=list,
        metadata=dict(
            name="int",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    long: List[Long] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    yes_no: List[YesNo] = field(
        default_factory=list,
        metadata=dict(
            name="yesNo",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    facet: List[Facet] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root:
    """
    :ivar generic:
    :ivar restricted:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    generic: Optional[Generic] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    restricted: Optional["Root.Restricted"] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )

    @dataclass
    class Restricted:
        """
        :ivar int_value:
        :ivar long:
        """
        int_value: List[IntType] = field(
            default_factory=list,
            metadata=dict(
                name="int",
                type="Element",
                min_occurs=1,
                max_occurs=9223372036854775807
            )
        )
        long: List[Long] = field(
            default_factory=list,
            metadata=dict(
                type="Element",
                min_occurs=1,
                max_occurs=9223372036854775807
            )
        )
