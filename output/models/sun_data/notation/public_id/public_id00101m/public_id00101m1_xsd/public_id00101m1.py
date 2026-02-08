from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "publicId"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "publicId"

    value: str = field(default="")
