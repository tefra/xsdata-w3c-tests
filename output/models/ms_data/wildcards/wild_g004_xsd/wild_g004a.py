from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://foo"


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"
        namespace = "http://foo"

    value: str = field(default="")
