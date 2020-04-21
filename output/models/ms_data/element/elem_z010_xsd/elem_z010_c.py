from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.element.elem_z010_xsd.elem_z010_d import (
    D,
)

__NAMESPACE__ = "c"


@dataclass
class C(D):
    """
    :ivar c:
    """
    class Meta:
        name = "c"

    c: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="c",
            required=True
        )
    )
