from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class B:
    abel_com_adam_com_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://abel.com/ http://adam.com/",
        },
    )


@dataclass(kw_only=True)
class E(B):
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Eden(E):
    class Meta:
        name = "eden"
