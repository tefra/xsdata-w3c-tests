from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.element.elem_z009_xsd.elem_z009_a import A

__NAMESPACE__ = "main"


@dataclass
class Ct:
    """
    :ivar a:
    """
    class Meta:
        name = "ct"

    a: Optional[A] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "main",
            "required": True,
        }
    )


@dataclass
class Root(Ct):
    class Meta:
        name = "root"
        namespace = "main"
