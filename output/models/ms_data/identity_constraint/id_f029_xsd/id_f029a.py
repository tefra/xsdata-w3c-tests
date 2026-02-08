from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "importNS"


@dataclass(kw_only=True)
class R:
    class Meta:
        name = "r"
        namespace = "importNS"

    value: str = field(default="")
