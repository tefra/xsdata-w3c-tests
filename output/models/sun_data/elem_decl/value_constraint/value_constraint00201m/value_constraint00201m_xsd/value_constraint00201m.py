from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Root:
    """
    :ivar twelve:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    twelve: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
