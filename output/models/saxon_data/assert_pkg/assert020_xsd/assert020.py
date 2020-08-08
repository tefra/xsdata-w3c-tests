from dataclasses import dataclass, field
from typing import List
from output.models.saxon_data.assert_pkg.assert020_xsd.assert020a import Temp

__NAMESPACE__ = "http://assert020.ns/"


@dataclass
class Doc:
    """
    :ivar temp:
    """
    class Meta:
        name = "doc"
        namespace = "http://assert020.ns/"

    temp: List[Temp] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
