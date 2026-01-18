from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from output.models.ms_data.particles.particles_js001_xsd.particles_js001_imp import (
    ImpElem1,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    local_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
        },
    )


@dataclass(kw_only=True)
class R(B):
    local_element: Any = field(
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
            "namespace": "",
            "required": True,
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
