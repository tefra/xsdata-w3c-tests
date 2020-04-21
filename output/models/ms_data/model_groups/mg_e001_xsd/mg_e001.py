from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar a:
    """
    class Meta:
        name = "test"

    a: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Root(Test):
    class Meta:
        name = "root"
