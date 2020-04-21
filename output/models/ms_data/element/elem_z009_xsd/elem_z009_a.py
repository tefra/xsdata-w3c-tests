from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.element.elem_z009_xsd.elem_z009_b import (
    B,
)

__NAMESPACE__ = "a"


@dataclass
class A(B):
    """
    :ivar a:
    """
    class Meta:
        name = "a"

    a: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="a",
            required=True
        )
    )
