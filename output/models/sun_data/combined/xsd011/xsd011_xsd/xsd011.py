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
    :ivar non_nillable_or_nillable1_or_nillable2:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    non_nillable_or_nillable1_or_nillable2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "non-nillable",
                    "type": NonNillable,
                },
                {
                    "name": "nillable1",
                    "type": Nillable1,
                },
                {
                    "name": "nillable2",
                    "type": List[int],
                    "min_length": 2,
                    "nillable": True,
                    "tokens": True,
                },
            ),
        }
    )
