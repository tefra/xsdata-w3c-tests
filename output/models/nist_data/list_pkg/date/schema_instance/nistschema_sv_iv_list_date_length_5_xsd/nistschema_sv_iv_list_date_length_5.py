from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-length-5-NS"


@dataclass
class NistschemaSvIvListDateLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-length-5"
        namespace = "NISTSchema-SV-IV-list-date-length-5-NS"

    value: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
        },
    )
