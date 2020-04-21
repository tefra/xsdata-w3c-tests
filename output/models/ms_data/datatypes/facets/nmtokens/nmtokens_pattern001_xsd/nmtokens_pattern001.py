from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar value:
    """
    class Meta:
        name = "foo"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"[A-C]{0,2}"
        )
    )
