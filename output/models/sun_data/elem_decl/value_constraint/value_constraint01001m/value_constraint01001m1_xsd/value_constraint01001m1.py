from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Id:
    """
    :ivar value:
    """
    class Meta:
        name = "ID"
        namespace = "ElemDecl/valueConstraint"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
