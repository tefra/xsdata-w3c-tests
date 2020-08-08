from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.particles.particles_jk005_xsd.particles_jk005_imp import ImpElem1

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar other_element:
    :ivar e1:
    """
    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##other"
        )
    )
    e1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class R:
    """
    :ivar other_element:
    :ivar imp_elem1:
    :ivar e1:
    """
    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##other"
        )
    )
    imp_elem1: Optional[ImpElem1] = field(
        default=None,
        metadata=dict(
            name="impElem1",
            type="Element",
            namespace="http://importedXSD"
        )
    )
    e1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
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
