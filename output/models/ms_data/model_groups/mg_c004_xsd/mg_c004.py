from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar a:
    :ivar b:
    :ivar c:
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
    c: Optional[object] = field(
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
