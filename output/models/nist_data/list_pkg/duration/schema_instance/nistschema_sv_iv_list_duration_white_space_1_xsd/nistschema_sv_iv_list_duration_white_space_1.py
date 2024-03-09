from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListDurationWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-duration-whiteSpace-1-NS"

    value: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        },
    )
