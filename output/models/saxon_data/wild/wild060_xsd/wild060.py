from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Zing1:
    class Meta:
        name = "zing"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ExtendedZing(Zing1):
    class Meta:
        name = "extendedZing"

    local_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )


@dataclass(kw_only=True)
class Zing(ExtendedZing):
    class Meta:
        name = "zing"
