from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class E:
    """
    :ivar value:
    """
    class Meta:
        namespace = "ElemDecl/valueConstraint"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"true"
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
