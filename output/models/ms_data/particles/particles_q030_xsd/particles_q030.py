from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_q030_xsd.particles_q030_imp import E2 as ParticlesQ030ImpE2
from output.models.ms_data.particles.particles_q030_xsd.particles_q030_imp2 import E2

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar foo:
    :ivar foo_bar_element:
    """
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    foo_bar_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "foo bar",
            "max_occurs": 4,
        }
    )


@dataclass
class R:
    """
    :ivar foo:
    :ivar foo_bar_element:
    :ivar e2:
    :ivar bar_e2:
    """
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    foo_bar_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "foo bar",
            "max_occurs": 4,
        }
    )
    e2: List[ParticlesQ030ImpE2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    bar_e2: List[E2] = field(
        default_factory=list,
        metadata={
            "name": "e2",
            "type": "Element",
            "namespace": "bar",
            "max_occurs": 2,
            "sequential": True,
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
