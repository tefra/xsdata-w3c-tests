from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_r020_xsd.particles_r020_imp import (
    ImpElem1,
    ImpElem2,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar foo:
    :ivar other_element:
    """
    foo: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            min_occurs=1,
            max_occurs=2
        )
    )


@dataclass
class R:
    """
    :ivar foo:
    :ivar other_element:
    :ivar imp_elem1:
    :ivar imp_elem2:
    """
    foo: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            min_occurs=1,
            max_occurs=2
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
    imp_elem2: Optional[ImpElem2] = field(
        default=None,
        metadata=dict(
            name="impElem2",
            type="Element",
            namespace="http://importedXSD"
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
