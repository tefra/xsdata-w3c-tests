from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from output.models.ms_data.particles.particles_jk004_xsd.particles_jk004_imp import (
    ImpElem1,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class R(B):
    other_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    imp_elem1: ImpElem1 = field(
        metadata={
            "name": "impElem1",
            "type": "Element",
            "namespace": "http://importedXSD",
        }
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | R = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
