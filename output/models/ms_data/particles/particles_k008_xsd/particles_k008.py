from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.particles.particles_k008_xsd.particles_k008_imp import ImpElem1

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    a0: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    imp_elem1: Optional[ImpElem1] = field(
        default=None,
        metadata={
            "name": "impElem1",
            "type": "Element",
            "namespace": "http://importedXSD",
            "required": True,
        }
    )
    a2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class R(B):
    pass


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
