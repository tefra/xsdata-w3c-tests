from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_q032_xsd.particles_q032_imp import E2 as ParticlesQ032ImpE2
from output.models.ms_data.particles.particles_q032_xsd.particles_q032_imp2 import E2 as ParticlesQ032Imp2E2

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar foo:
    :ivar target_namespace_foo_bar_element:
    """
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
    """
    :ivar any_element:
    """
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
    """
    :ivar foo:
    :ivar target_namespace_foo_bar_element:
    :ivar e2:
    :ivar e2_1:
    :ivar e2_2:
    """
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
    e2: List[ParticlesQ032ImpE2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "max_occurs": 2,
        }
    )
    e2_1: Optional[E2] = field(
        default=None,
        metadata={
            "name": "e2",
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )
    e2_2: Optional[ParticlesQ032Imp2E2] = field(
        default=None,
        metadata={
            "name": "e2",
            "type": "Element",
            "namespace": "bar",
        }
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
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
