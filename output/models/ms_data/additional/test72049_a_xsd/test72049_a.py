from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    a: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
