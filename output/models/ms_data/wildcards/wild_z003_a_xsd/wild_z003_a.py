from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.wildcards.wild_z003_a_xsd.wild_z003_b import Elem

__NAMESPACE__ = "urn:foo"


@dataclass
class Elt1:
    class Meta:
        name = "elt1"
        namespace = "urn:foo"

    elt2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:bar",
            "required": True,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "max_occurs": 3,
        }
    )
