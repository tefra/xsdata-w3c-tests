from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "tns"


@dataclass
class ChildType:
    """
    :ivar content:
    :ivar type1:
    :ivar type2:
    """
    class Meta:
        name = "childType"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type1: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    type2: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class DerivedType1(ChildType):
    """
    :ivar value:
    """
    class Meta:
        name = "derivedType1"

    value: Optional[bool] = field(
        default=None,
    )


@dataclass
class DerivedType2(ChildType):
    """
    :ivar value:
    """
    class Meta:
        name = "derivedType2"

    value: Optional[int] = field(
        default=None,
    )


@dataclass
class Root:
    """
    :ivar child:
    """
    class Meta:
        name = "root"
        namespace = "tns"

    child: List[Union[ChildType, DerivedType1, DerivedType2]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
