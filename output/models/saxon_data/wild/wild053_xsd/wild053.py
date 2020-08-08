from dataclasses import dataclass, field
from typing import Optional
from output.models.saxon_data.wild.wild053_xsd.wild053imp import Zing


@dataclass
class Zang:
    """
    :ivar any_element:
    """
    class Meta:
        name = "zang"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
