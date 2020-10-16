from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_q020_xsd.particles_q020_imp import Bar

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar foo:
    :ivar other_element:
    """
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "required": True,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "max_occurs": 4,
        }
    )


@dataclass
class R:
    """
    :ivar foo:
    :ivar other_element:
    :ivar bar:
    """
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "required": True,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "max_occurs": 4,
        }
    )
    bar: List[Bar] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
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
