from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_jf003_xsd.particles_jf003_imp import ImpElem1

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
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
            "min_occurs": 1,
            "max_occurs": 9999999,
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
