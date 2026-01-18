from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "name"


@dataclass(kw_only=True)
class Test1:
    class Meta:
        name = "Test"

    abc: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Test(Test1):
    class Meta:
        name = "test"
        namespace = "name"
