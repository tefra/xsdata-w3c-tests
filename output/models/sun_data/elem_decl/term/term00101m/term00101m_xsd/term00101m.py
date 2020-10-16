from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/term"


@dataclass
class Local:
    """
    :ivar value:
    """
    class Meta:
        namespace = "ElemDecl/term"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar local:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/term"

    local: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "required": True,
        }
    )
