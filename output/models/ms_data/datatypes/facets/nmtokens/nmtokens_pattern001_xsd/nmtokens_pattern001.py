from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[A-C]{0,2}",
            "tokens": True,
        },
    )
