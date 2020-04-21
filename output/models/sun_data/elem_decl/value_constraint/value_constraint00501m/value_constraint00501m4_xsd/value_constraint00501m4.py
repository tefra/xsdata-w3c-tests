from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Element:
    """
    :ivar value:
    """
    class Meta:
        namespace = "ElemDecl/valueConstraint"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"...[Ee].."
        )
    )


@dataclass
class Root:
    """
    :ivar element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    element: Optional[Element] = field(
        default=None,
        metadata=dict(
            name="Element",
            type="Element",
            required=True
        )
    )
