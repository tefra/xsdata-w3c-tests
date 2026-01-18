from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from output.models.ms_data.particles.particles_jm005_xsd.particles_jm005_imp import (
    ImpElem1,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    foo_imported_xsd_bar_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "foo http://importedXSD bar",
            "max_occurs": 3,
        },
    )


@dataclass(kw_only=True)
class R(B):
    foo_imported_xsd_bar_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    imp_elem1: list[ImpElem1] = field(
        default_factory=list,
        metadata={
            "name": "impElem1",
            "type": "Element",
            "namespace": "http://importedXSD",
            "min_occurs": 2,
            "max_occurs": 3,
        },
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
