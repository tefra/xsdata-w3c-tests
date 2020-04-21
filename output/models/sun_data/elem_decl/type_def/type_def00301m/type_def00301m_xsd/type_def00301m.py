from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Local:
    """
    :ivar value:
    """
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar local:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    local: Optional[Local] = field(
        default=None,
        metadata=dict(
            name="Local",
            type="Element",
            required=True
        )
    )
