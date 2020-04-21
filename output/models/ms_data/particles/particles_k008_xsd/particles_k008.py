from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.particles.particles_k008_xsd.particles_k008_imp import (
    ImpElem1,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar a0:
    :ivar imp_elem1:
    :ivar a2:
    """
    a0: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    imp_elem1: Optional[ImpElem1] = field(
        default=None,
        metadata=dict(
            name="impElem1",
            type="Element",
            namespace="http://importedXSD",
            required=True
        )
    )
    a2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class R:
    """
    :ivar a0:
    :ivar imp_elem1:
    :ivar a2:
    """
    a0: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    imp_elem1: Optional[ImpElem1] = field(
        default=None,
        metadata=dict(
            name="impElem1",
            type="Element",
            namespace="http://importedXSD",
            required=True
        )
    )
    a2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
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
