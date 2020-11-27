from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "contentType"


@dataclass
class A1:
    class Meta:
        name = "A"

    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "contentType"
