from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional, Union

__NAMESPACE__ = "urn:test"


class Myunion2Value(Enum):
    A = "a"
    B = "b"


@dataclass
class Info2:
    class Meta:
        name = "info2"
        namespace = "urn:test"

    value: Optional[Union[Decimal, Myunion2Value]] = field(
        default=None
    )
