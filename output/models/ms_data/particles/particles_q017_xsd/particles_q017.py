from dataclasses import dataclass, field
from typing import Optional

from output.models.ms_data.particles.particles_q017_xsd.particles_q017_imp import (
    Foo,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 4,
        },
    )


@dataclass
class R:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )
    foo_foo: list[Foo] = field(
        default_factory=list,
        metadata={
            "name": "foo",
            "type": "Element",
            "namespace": "foo",
            "max_occurs": 2,
        },
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
            "required": True,
        },
    )
