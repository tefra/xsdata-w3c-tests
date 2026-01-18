from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://eden.com/"


@dataclass(kw_only=True)
class Eden:
    class Meta:
        name = "eden"
        namespace = "http://eden.com/"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
