from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-length-4-NS"


@dataclass
class NistschemaSvIvListGYearLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-length-4"
        namespace = "NISTSchema-SV-IV-list-gYear-length-4-NS"

    value: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 8,
            "tokens": True,
        }
    )
