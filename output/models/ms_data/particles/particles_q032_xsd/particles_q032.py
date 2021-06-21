from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_q032_xsd.particles_q032_imp import E2 as ParticlesQ032ImpE2
from output.models.ms_data.particles.particles_q032_xsd.particles_q032_imp2 import E2 as ParticlesQ032Imp2E2

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    target_namespace_foo_bar_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace foo bar",
            "max_occurs": 4,
        }
    )


@dataclass
class E2:
    class Meta:
        name = "e2"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class R:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    target_namespace_foo_bar_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace foo bar",
            "max_occurs": 4,
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e2",
                    "type": ParticlesQ032ImpE2,
                    "namespace": "foo",
                },
                {
                    "name": "e2",
                    "type": E2,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "e2",
                    "type": ParticlesQ032Imp2E2,
                    "namespace": "bar",
                },
            ),
            "max_occurs": 2,
        }
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
        }
    )
