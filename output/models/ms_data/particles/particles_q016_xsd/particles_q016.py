from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_q016_xsd.particles_q016_imp import Foo

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 4,
        }
    )


@dataclass
class R:
    xsdtesting_foo: Optional[object] = field(
        default=None,
        metadata={
            "name": "foo",
            "type": "Element",
            "namespace": "http://xsdtesting",
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 4,
        }
    )
    foo: List[Foo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
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
        }
    )
