from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.wildcards.wild_z003_a_xsd.wild_z003_b import (
    Elem,
)

__NAMESPACE__ = "urn:foo"


@dataclass
class Elt1:
    """
    :ivar elt2:
    :ivar elem:
    :ivar other_element:
    """
    class Meta:
        name = "elt1"
        namespace = "urn:foo"

    elt2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    elem: Optional[Elem] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:bar",
            required=True
        )
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            min_occurs=1,
            max_occurs=3
        )
    )