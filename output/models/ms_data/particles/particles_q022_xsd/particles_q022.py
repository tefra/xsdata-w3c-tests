from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_q022_xsd.particles_q022_imp import Foo

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar foo:
    :ivar local_element:
    """
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "required": True,
        }
    )
    local_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "max_occurs": 4,
        }
    )


@dataclass
class R:
    """
    :ivar foo:
    :ivar local_element:
    :ivar xsdtesting_foo:
    """
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "required": True,
        }
    )
    local_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "max_occurs": 4,
        }
    )
    xsdtesting_foo: List[Foo] = field(
        default_factory=list,
        metadata={
            "name": "foo",
            "type": "Element",
            "namespace": "http://xsdtesting",
            "max_occurs": 2,
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
        }
    )
