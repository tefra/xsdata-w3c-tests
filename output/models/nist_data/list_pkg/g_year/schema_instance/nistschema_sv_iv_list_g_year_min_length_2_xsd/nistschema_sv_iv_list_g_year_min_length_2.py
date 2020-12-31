from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-minLength-2-NS"


@dataclass
class NistschemaSvIvListGYearMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-minLength-2"
        namespace = "NISTSchema-SV-IV-list-gYear-minLength-2-NS"

    value: List[Period] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 6,
            "tokens": True,
        }
    )
