from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class C:
    """
    :ivar any_element:
    """
    class Meta:
        name = "c"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar p:
    """
    class Meta:
        name = "root"
        namespace = "a"

    p: Optional[C] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
