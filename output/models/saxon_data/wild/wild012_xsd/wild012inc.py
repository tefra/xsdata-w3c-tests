from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://eden.com/"


@dataclass(kw_only=True)
class Eden:
    class Meta:
        name = "eden"
        namespace = "http://eden.com/"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
