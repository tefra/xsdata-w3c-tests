from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "psContents"


@dataclass
class A:
    """
    :ivar any_element:
    """
    class Meta:
        name = "a"
        namespace = "psContents"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Date:
    """
    :ivar value:
    """
    class Meta:
        name = "date"
        namespace = "psContents"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
