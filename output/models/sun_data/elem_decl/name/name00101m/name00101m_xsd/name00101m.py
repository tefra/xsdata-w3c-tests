from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root2:
    """
    :ivar value:
    """
    class Meta:
        name = "root2"
        namespace = "ElemDecl/name"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )