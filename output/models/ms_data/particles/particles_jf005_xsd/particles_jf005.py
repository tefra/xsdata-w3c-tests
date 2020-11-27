from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.particles.particles_jf005_xsd.particles_jf005_imp import ImpElem1

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
    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class R:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
    imp_elem1: Optional[ImpElem1] = field(
        default=None,
        metadata={
            "name": "impElem1",
            "type": "Element",
            "namespace": "http://importedXSD",
        }
    )
    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
        }
    )
