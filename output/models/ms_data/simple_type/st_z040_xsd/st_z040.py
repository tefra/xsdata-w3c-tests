from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional, Union

__NAMESPACE__ = "urn:test"


@dataclass
class Info2:
    class Meta:
        name = "info2"
        namespace = "urn:test"

    value: Optional[Union[Decimal, "Info2.Value"]] = field(
        default=None,
        metadata={
            "required": True,
        }
    )

    class Value(Enum):
        A = "a"
        B = "b"
