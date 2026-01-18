from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Beta:
    class Meta:
        name = "beta"

    open_com_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
        },
    )
