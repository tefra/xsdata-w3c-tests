from dataclasses import dataclass, field
from decimal import Decimal
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
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Sub:
        """
        :ivar idelt:
        """
        idelt: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
