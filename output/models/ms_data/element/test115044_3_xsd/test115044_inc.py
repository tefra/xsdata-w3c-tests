from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class E1:
    class Meta:
        name = "e1"
        namespace = "foo"

    value: int = field()
