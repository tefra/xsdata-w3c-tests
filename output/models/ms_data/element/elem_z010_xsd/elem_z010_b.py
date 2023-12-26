from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.element.elem_z010_xsd.elem_z010_c import C

__NAMESPACE__ = "b"


@dataclass
class B(C):
    class Meta:
        name = "b"

    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "b",
        },
    )
