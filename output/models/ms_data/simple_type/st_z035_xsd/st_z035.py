from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "foo"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"[b|c]+",
        }
    )
