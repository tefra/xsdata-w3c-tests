from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "derivationMethod"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "derivationMethod"

    value: Optional[int] = field(
        default=None
    )
