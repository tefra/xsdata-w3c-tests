from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.particles.particles_q032_xsd.particles_q032_imp2 import (
    E2 as ParticlesQ032Imp2E2,
)
from output.models.ms_data.particles.particles_q032_xsd.particles_q032_imp import (
    E2 as ParticlesQ032ImpE2,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar foo:
    :ivar target_namespace_foo_bar_element:
    """
    foo: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    target_namespace_foo_bar_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##targetNamespace foo bar",
            min_occurs=0,
            max_occurs=4
        )
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
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class R:
    """
    :ivar foo:
    :ivar target_namespace_foo_bar_element:
    :ivar foo_e2:
    :ivar xsdtesting_e2:
    :ivar e2:
    """
    foo: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    target_namespace_foo_bar_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##targetNamespace foo bar",
            min_occurs=0,
            max_occurs=4
        )
    )
    foo_e2: List[ParticlesQ032ImpE2] = field(
        default_factory=list,
        metadata=dict(
            name="e2",
            type="Element",
            namespace="foo",
            min_occurs=0,
            max_occurs=2
        )
    )
    xsdtesting_e2: Optional[E2] = field(
        default=None,
        metadata=dict(
            name="e2",
            type="Element",
            namespace="http://xsdtesting"
        )
    )
    e2: Optional[ParticlesQ032Imp2E2] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="bar"
        )
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
        metadata=dict(
            type="Element",
            namespace=""
        )
    )