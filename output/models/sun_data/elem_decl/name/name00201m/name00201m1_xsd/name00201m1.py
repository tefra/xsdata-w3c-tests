from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Root:
    """
    :ivar true_value:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    true_value: Optional[object] = field(
        default=None,
        metadata=dict(
            name="true",
            type="Element",
            namespace="",
            required=True
        )
    )
