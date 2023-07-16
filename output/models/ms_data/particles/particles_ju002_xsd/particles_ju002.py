from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_ju002_xsd.particles_ju002_imp import ImpElem1

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    local_foo_target_namespace_imported_xsd_bar_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": (
                "##local foo ##targetNamespace http://importedXSD bar"
            ),
            "max_occurs": 10,
        }
    )


@dataclass
class R(B):
    imp_elem1: List[ImpElem1] = field(
        default_factory=list,
        metadata={
            "name": "impElem1",
            "type": "Element",
            "namespace": "http://importedXSD",
            "min_occurs": 2,
            "max_occurs": 5,
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
