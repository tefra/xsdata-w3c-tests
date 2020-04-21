from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.element.test115044_3_xsd.test115044_inc import (
    E1,
)

__NAMESPACE__ = "foo"


@dataclass
class E:
    """
    :ivar any_element:
    """
    class Meta:
        name = "e"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar e1:
    :ivar e:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    e1: Optional[E1] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    e: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
