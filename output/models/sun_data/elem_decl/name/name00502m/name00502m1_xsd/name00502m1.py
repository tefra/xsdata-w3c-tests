from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Global1:
    """
    :ivar local:
    """
    class Meta:
        namespace = "ElemDecl/name"

    local: Optional[object] = field(
        default=None,
        metadata=dict(
            name="Local",
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Global2:
    """
    :ivar local:
    """
    class Meta:
        namespace = "ElemDecl/name"

    local: Optional[object] = field(
        default=None,
        metadata=dict(
            name="Local",
            type="Element",
            namespace="",
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
        namespace = "ElemDecl/name"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )