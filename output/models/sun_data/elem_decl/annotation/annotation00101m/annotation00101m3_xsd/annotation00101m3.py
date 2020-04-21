from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/annotation"


@dataclass
class Test:
    class Meta:
        namespace = "ElemDecl/annotation"


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
