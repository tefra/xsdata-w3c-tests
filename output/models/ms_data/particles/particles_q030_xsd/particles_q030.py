from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.particles.particles_q030_xsd.particles_q030_imp import (
    E2 as ImpE2,
)
from output.models.ms_data.particles.particles_q030_xsd.particles_q030_imp2 import (
    E2 as Imp2E2,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    foo: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    foo_bar_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "foo bar",
            "max_occurs": 4,
        },
    )


@dataclass(kw_only=True)
class R:
    foo: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e2: list[ImpE2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    bar_e2: list[Imp2E2] = field(
        default_factory=list,
        metadata={
            "name": "e2",
            "type": "Element",
            "namespace": "bar",
            "max_occurs": 2,
            "sequence": 1,
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
