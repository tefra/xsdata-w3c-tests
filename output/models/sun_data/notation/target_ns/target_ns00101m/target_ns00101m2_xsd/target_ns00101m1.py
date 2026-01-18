from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "tck_test"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "tck_test"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
