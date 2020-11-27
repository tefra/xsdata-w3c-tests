from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.element.elem_z010_xsd.elem_z010_b import B

__NAMESPACE__ = "a"


@dataclass
class A(B):
    class Meta:
        name = "a"

    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
