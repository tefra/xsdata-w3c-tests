from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "MGroupDef/annotation"


@dataclass
class A:
    """
    :ivar c:
    :ivar date:
    """
    c: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    date: Optional[str] = field(
        default=None,
        metadata=dict(
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
        namespace = "MGroupDef/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
