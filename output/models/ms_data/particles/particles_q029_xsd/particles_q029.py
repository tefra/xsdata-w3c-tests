from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.particles.particles_q029_xsd.particles_q029_imp import (
    E2,
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
    e2: E2 = field(
        metadata={
            "type": "Element",
            "namespace": "foo",
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
