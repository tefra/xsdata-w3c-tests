from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Elt1:
    """
    :ivar any_element:
    """
    class Meta:
        name = "elt1"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Elt2:
    """
    :ivar value:
    """
    class Meta:
        name = "elt2"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar elt1:
    """
    class Meta:
        name = "root"

    elt1: List[Elt1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
