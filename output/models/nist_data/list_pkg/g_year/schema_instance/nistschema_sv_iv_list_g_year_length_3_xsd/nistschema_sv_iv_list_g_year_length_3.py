from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-length-3-NS"


@dataclass
class NistschemaSvIvListGYearLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-length-3"
        namespace = "NISTSchema-SV-IV-list-gYear-length-3-NS"

    value: List[Period] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 7,
            "tokens": True,
        }
    )
