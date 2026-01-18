from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Computer1:
    class Meta:
        name = "computer"

    local_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )


@dataclass(kw_only=True)
class ExtendedComputer(Computer1):
    class Meta:
        name = "extendedComputer"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Computer(ExtendedComputer):
    class Meta:
        name = "computer"
