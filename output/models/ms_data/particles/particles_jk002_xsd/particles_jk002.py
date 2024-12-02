from dataclasses import dataclass, field
from typing import Any, Optional

from output.models.ms_data.particles.particles_jk002_xsd.particles_jk002_imp import (
    ImpElem1,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
class R(B):
    other_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    imp_elem1: Optional[ImpElem1] = field(
        default=None,
        metadata={
            "name": "impElem1",
            "type": "Element",
            "namespace": "http://importedXSD",
            "required": True,
        },
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
        },
    )
