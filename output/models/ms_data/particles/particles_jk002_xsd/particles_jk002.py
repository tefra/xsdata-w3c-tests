from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_jk002_xsd.particles_jk002_imp import ImpElem1

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar other_element:
    """
    other_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            min_occurs=1,
            max_occurs=9223372036854775807
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
