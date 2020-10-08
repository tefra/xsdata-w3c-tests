from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Type:
    """
    :ivar value:
    """
    class Meta:
        name = "_-."
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Type0:
    """
    :ivar value:
    """
    class Meta:
        name = "_-0."
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar value:
    :ivar value_0:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="_-.",
            type="Element",
            required=True
        )
    )
    value_0: Optional[int] = field(
        default=None,
        metadata=dict(
            name="_-0.",
            type="Element",
            required=True
        )
    )
