from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar sub:
    """
    class Meta:
        name = "root"

    sub: List["Root.Sub"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Sub:
        """
        :ivar idelt:
        """
        idelt: Optional[Decimal] = field(
            default=None,
            metadata=dict(
                type="Element",
                namespace="",
                required=True
            )
        )
