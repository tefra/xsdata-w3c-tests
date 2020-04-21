from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Global1:
    """
    :ivar value:
    """
    class Meta:
        namespace = "ElemDecl/name"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Global2:
    """
    :ivar value:
    """
    class Meta:
        namespace = "ElemDecl/name"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
