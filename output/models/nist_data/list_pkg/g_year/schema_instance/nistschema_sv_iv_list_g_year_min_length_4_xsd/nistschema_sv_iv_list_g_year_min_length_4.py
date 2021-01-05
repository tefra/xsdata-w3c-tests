from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-minLength-4-NS"


@dataclass
class NistschemaSvIvListGYearMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-minLength-4"
        namespace = "NISTSchema-SV-IV-list-gYear-minLength-4-NS"

    value: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 8,
            "tokens": True,
        }
    )
