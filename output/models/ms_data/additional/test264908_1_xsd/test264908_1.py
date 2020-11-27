from dataclasses import dataclass, field
from typing import Optional


@dataclass
class T:
    class Meta:
        name = "t"

    blah: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
