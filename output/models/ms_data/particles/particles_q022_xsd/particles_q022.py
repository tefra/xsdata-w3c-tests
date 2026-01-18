from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.particles.particles_q022_xsd.particles_q022_imp import (
    Foo,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    foo: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )
    local_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "max_occurs": 4,
        },
    )


@dataclass(kw_only=True)
class R:
    xsdtesting_foo: None | object = field(
        default=None,
        metadata={
            "name": "foo",
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )
    foo: list[Foo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
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
        },
    )
