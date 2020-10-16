from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/nillable"


@dataclass
class GlobalType:
    """
    :ivar any_element:
    """
    class Meta:
        name = "Global"
        nillable = True
        namespace = "ElemDecl/nillable"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/nillable"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
