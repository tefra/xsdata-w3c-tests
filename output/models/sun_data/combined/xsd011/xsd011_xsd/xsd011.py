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
        metadata={
            "type": "Element",
            "required": True,
        }
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
        metadata={
            "min_length": 2,
            "tokens": True,
        }
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
        metadata={
            "type": "Element",
            "required": True,
        }
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
        metadata={
            "name": "non-nillable",
            "type": "Element",
        }
    )
    nillable1: List[Nillable1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    nillable2: List[List[int]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_length": 2,
            "nillable": True,
            "tokens": True,
        }
    )
