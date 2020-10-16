from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/abstract"


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/abstract"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
