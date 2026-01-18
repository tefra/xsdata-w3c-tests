from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    foo: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    bar: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class T(Test):
    pass
