from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.particles.particles_jf015_xsd.particles_jf015_imp import ImpElem1

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class R(B):
    imp_elem1: Optional[ImpElem1] = field(
        default=None,
        metadata={
            "name": "impElem1",
            "type": "Element",
            "namespace": "http://importedXSD",
            "required": True,
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
