from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    a: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Root(Test):
    class Meta:
        name = "root"
