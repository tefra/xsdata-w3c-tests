from dataclasses import dataclass, field
from typing import Optional
from output.models.saxon_data.wild.wild053_xsd.wild053imp import Zing


@dataclass
class Zang:
    class Meta:
        name = "zang"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
