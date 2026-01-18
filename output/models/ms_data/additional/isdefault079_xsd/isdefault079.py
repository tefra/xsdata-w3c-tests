from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class RegistryValueModOpSetType:
    regvalueop: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )


@dataclass(kw_only=True)
class Regvaluemodopset(RegistryValueModOpSetType):
    class Meta:
        name = "regvaluemodopset"
