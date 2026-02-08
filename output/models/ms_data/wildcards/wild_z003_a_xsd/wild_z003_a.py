from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.wildcards.wild_z003_a_xsd.wild_z003_b import Elem

__NAMESPACE__ = "urn:foo"


@dataclass(kw_only=True)
class Elt1:
    class Meta:
        name = "elt1"
        namespace = "urn:foo"

    elt2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    elem: Elem = field(
        metadata={
            "type": "Element",
            "namespace": "urn:bar",
        }
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "max_occurs": 3,
        },
    )
