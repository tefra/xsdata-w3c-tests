from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            pattern=r"[01]+"
        )
    )