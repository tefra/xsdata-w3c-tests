from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class T:
    adam_com_eve_com_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://adam.com/ http://eve.com/",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Eden(T):
    class Meta:
        name = "eden"
