from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.example.org"


@dataclass
class X:
    """
    :ivar y:
    """
    class Meta:
        name = "x"
        namespace = "http://www.example.org"

    y: Optional["X.Y"] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )

    @dataclass
    class Y:
        pass
