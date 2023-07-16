from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_r020_xsd.particles_r020_imp import (
    ImpElem1,
    ImpElem2,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "max_occurs": 2,
        }
    )


@dataclass
class R:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    imp_elem1_or_imp_elem2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "impElem1",
                    "type": ImpElem1,
                    "namespace": "http://importedXSD",
                },
                {
                    "name": "impElem2",
                    "type": ImpElem2,
                    "namespace": "http://importedXSD",
                },
            ),
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
