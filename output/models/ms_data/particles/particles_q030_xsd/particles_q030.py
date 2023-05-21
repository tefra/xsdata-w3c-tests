from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_q030_xsd.particles_q030_imp import E2 as ImpE2
from output.models.ms_data.particles.particles_q030_xsd.particles_q030_imp2 import E2 as Imp2E2

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    e2: List[ImpE2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "max_occurs": 2,
            "sequence": 1,
        }
    )
    bar_e2: List[Imp2E2] = field(
        default_factory=list,
        metadata={
            "name": "e2",
            "type": "Element",
            "namespace": "bar",
            "max_occurs": 2,
            "sequence": 1,
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
