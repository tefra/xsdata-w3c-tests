from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AD_annotation"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AD_annotation"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
