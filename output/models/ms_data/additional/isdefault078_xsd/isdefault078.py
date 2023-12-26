from dataclasses import dataclass, field
from typing import Optional
from output.models.ms_data.additional.isdefault078_xsd.xml import SpaceValue


@dataclass
class Root:
    class Meta:
        name = "root"

    space: Optional[SpaceValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
