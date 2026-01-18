from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.particles.particles_r020_xsd.particles_r020_imp import (
    ImpElem1,
    ImpElem2,
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
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "max_occurs": 2,
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
    imp_elem1_or_imp_elem2: None | ImpElem1 | ImpElem2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "impElem1",
                    "type": ImpElem1,
                    "namespace": "http://importedXSD",
                },
                {
                    "name": "impElem2",
                    "type": ImpElem2,
                    "namespace": "http://importedXSD",
                },
            ),
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
