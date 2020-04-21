from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Union

__NAMESPACE__ = "urn:test"


@dataclass
class Info2:
    """
    :ivar value:
    """
    class Meta:
        name = "info2"
        namespace = "urn:test"

    value: Optional[Union[Decimal, "Info2.Value"]] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )

    class Value(Enum):
        """
        :cvar A:
        :cvar B:
        """
        A = "a"
        B = "b"
