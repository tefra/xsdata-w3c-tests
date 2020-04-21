from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "name"


@dataclass
class Test:
    """
    :ivar abc:
    """
    abc: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Test(Test):
    class Meta:
        name = "test"
        namespace = "name"
