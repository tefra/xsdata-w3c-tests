from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:uuid:48D2A016-64FF-4e20-B7F0-FE15842C4D1B/"


@dataclass(kw_only=True)
class Series:
    class Meta:
        name = "series"
        namespace = "urn:uuid:48D2A016-64FF-4e20-B7F0-FE15842C4D1B/"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
