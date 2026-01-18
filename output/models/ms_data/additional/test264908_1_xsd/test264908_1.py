from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"

    blah: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
