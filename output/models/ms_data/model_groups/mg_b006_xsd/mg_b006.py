from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"

    foo: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Root(Bar):
    class Meta:
        name = "root"
