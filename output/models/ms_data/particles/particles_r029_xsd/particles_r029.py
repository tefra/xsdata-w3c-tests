from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.particles.particles_r029_xsd.particles_r029_imp import (
    ImpElem1,
)

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar foo:
    :ivar foo_bar_element:
    """
    foo: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    foo_bar_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="foo bar",
            required=True
        )
    )


@dataclass
class R:
    """
    :ivar foo:
    :ivar foo_bar_element:
    :ivar imp_elem1:
    """
    foo: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    foo_bar_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="foo bar",
            required=True
        )
    )
    imp_elem1: Optional[ImpElem1] = field(
        default=None,
        metadata=dict(
            name="impElem1",
            type="Element",
            namespace="foo"
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
