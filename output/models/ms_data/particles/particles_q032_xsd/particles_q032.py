from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.particles.particles_q032_xsd.particles_q032_imp import (
    E2 as ImpE2,
)
from output.models.ms_data.particles.particles_q032_xsd.particles_q032_imp2 import (
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
    target_namespace_foo_bar_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace foo bar",
            "max_occurs": 4,
        },
    )


@dataclass(kw_only=True)
class E2:
    class Meta:
        name = "e2"
        namespace = "http://xsdtesting"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
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
    e2: list[ImpE2 | E2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e2",
                    "type": ImpE2,
                    "namespace": "foo",
                    "max_occurs": 2,
                },
                {
                    "name": "e2",
                    "type": E2,
                    "namespace": "http://xsdtesting",
                },
            ),
            "max_occurs": 3,
        },
    )
    e2_2: None | Imp2E2 = field(
        default=None,
        metadata={
            "name": "e2",
            "type": "Element",
            "namespace": "bar",
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
