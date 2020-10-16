from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_je008_xsd.particles_je008_imp import ImpElem1

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar any_element:
    """
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )


@dataclass
class R(B):
    """
    :ivar imp_elem1:
    """
    imp_elem1: List[ImpElem1] = field(
        default_factory=list,
        metadata={
            "name": "impElem1",
            "type": "Element",
            "namespace": "http://importedXSD",
            "min_occurs": 2,
            "max_occurs": 2,
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
