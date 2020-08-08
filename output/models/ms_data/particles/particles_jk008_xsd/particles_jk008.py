from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.particles.particles_jk008_xsd.particles_jk008_imp import ImpElem1

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar other_element:
    """
    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            required=True
        )
    )


@dataclass
class R(B):
    """
    :ivar imp_elem1:
    """
    imp_elem1: Optional[ImpElem1] = field(
        default=None,
        metadata=dict(
            name="impElem1",
            type="Element",
            namespace="http://importedXSD",
            required=True
        )
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
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
