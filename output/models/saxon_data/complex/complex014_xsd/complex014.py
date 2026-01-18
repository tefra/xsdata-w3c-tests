from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        nillable = True

    e: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    f: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
