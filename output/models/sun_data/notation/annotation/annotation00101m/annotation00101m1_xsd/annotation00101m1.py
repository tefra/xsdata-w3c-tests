from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "Notation/annotation"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "Notation/annotation"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
