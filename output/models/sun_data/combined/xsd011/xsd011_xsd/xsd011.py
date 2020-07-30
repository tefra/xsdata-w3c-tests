from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class Nillable1:
    """
    :ivar x:
    """
    class Meta:
        name = "nillable1"
        nillable = True
        namespace = "foo"

    x: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Nillable2:
    """
    :ivar value:
    """
    class Meta:
        name = "nillable2"
        nillable = True
        namespace = "foo"

    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_length=2
        )
    )


@dataclass
class NonNillable:
    """
    :ivar x:
    """
    class Meta:
        name = "non-nillable"
        namespace = "foo"

    x: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar non_nillable:
    :ivar nillable1:
    :ivar nillable2:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    non_nillable: List[NonNillable] = field(
        default_factory=list,
        metadata=dict(
            name="non-nillable",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    nillable1: List[Nillable1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    nillable2: List[Nillable2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
