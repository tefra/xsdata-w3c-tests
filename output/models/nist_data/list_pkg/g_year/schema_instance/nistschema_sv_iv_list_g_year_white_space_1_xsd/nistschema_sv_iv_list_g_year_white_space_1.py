from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListGYearWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-gYear-whiteSpace-1-NS"

    value: List[Period] = field(
        default_factory=list,
        metadata={
            "required": True,
            "white_space": "collapse",
            "tokens": True,
        }
    )
