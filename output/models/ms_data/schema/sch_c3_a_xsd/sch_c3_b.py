from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CtB:
    """
    :ivar b1:
    :ivar b2:
    """
    class Meta:
        name = "ct-B"

    b1: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class E2(CtB):
    class Meta:
        name = "e2"
