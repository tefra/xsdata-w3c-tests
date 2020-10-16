from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_q029_xsd.particles_q029_imp import E2

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
            "min_occurs": 1,
            "max_occurs": 4,
        }
    )


@dataclass
class R:
    """
    :ivar foo:
    :ivar foo_bar_element:
    :ivar e2:
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
            "min_occurs": 1,
            "max_occurs": 4,
        }
    )
    e2: Optional[E2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
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
