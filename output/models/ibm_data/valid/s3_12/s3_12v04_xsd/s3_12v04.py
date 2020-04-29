from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://xstest-tns"


@dataclass
class AnySimpleType:
    """
    :ivar value:
    :ivar type:
    """
    class Meta:
        name = "anySimpleType"

    value: Optional[object] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class DoubleType:
    """
    :ivar value:
    :ivar type:
    """
    class Meta:
        name = "doubleType"

    value: Optional[Decimal] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class FloatType:
    """
    :ivar value:
    :ivar type:
    """
    class Meta:
        name = "floatType"

    value: Optional[float] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar elem1:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    elem1: List[Union[AnySimpleType, DoubleType, FloatType]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=5
        )
    )
