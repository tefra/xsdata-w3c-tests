from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"...E.."
        )
    )