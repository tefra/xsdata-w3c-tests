from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://eden.com/"


@dataclass
class Eden:
    """
    :ivar any_element:
    """
    class Meta:
        name = "eden"
        namespace = "http://eden.com/"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )