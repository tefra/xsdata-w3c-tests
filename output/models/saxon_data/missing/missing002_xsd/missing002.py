from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bad:
    """
    :ivar any_element:
    """
    class Meta:
        name = "bad"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Good:
    """
    :ivar value:
    """
    class Meta:
        name = "good"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Perfect:
    """
    :ivar any_element:
    """
    class Meta:
        name = "perfect"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
