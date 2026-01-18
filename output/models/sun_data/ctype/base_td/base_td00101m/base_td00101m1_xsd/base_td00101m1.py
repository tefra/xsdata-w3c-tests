from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "baseTD"


@dataclass(kw_only=True)
class Test2:
    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Test(Test2):
    pass


@dataclass(kw_only=True)
class Root(Test):
    class Meta:
        name = "root"
        namespace = "baseTD"
