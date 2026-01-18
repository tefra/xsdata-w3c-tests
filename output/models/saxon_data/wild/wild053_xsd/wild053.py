from __future__ import annotations

from dataclasses import dataclass, field

from output.models.saxon_data.wild.wild053_xsd.wild053imp import Zing


@dataclass(kw_only=True)
class Zang:
    class Meta:
        name = "zang"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root(Zing):
    class Meta:
        name = "root"
