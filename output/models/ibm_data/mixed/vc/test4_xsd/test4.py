from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class TestV2:
    class Meta:
        name = "TEST_V2"

    value: int = field()
    v2: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Test(TestV2):
    class Meta:
        name = "test"
