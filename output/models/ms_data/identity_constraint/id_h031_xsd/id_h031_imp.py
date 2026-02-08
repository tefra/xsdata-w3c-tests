from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "importNS"


@dataclass(kw_only=True)
class Iid:
    class Meta:
        name = "iid"
        namespace = "importNS"

    value: str = field(default="")
    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "importNS",
        },
    )
