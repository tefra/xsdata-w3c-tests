from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.particles.particles_jm004_xsd.particles_jm004_imp import ImpElem1

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar foo_imported_xsd_bar_element:
    """
    foo_imported_xsd_bar_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "foo http://importedXSD bar",
            "required": True,
        }
    )


@dataclass
class R(B):
    """
    :ivar imp_elem1:
    """
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
    """
    :ivar elem:
    """
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
