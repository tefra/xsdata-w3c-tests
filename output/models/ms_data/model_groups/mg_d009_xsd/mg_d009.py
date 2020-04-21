from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "test"

    a: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    b: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class Root(Test):
    class Meta:
        name = "root"
