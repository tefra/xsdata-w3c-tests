from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Global:
    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
