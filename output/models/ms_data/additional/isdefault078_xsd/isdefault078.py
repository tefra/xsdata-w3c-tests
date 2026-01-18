from __future__ import annotations

from dataclasses import dataclass, field

from output.models.ms_data.additional.isdefault078_xsd.xml import SpaceValue


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    space: None | SpaceValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
