from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Temp:
    """
    :ivar a:
    :ivar x:
    :ivar y:
    """
    class Meta:
        name = "temp"

    a: Optional["Temp.A"] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    x: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    y: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    @dataclass
    class A:
        """
        :ivar b:
        """
        b: Optional[object] = field(
            default=None,
            metadata=dict(
                type="Element"
            )
        )
