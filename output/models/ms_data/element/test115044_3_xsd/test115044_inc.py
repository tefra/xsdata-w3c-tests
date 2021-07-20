from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class E1:
    class Meta:
        name = "e1"
        namespace = "foo"

    value: Optional[int] = field(
        default=None
    )
