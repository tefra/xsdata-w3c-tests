from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Root:
    """
    :ivar content:
    :ivar separator:
    :ivar attr:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    separator: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    attr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
