from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-length-2-NS"


@dataclass
class NistschemaSvIvListDateLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-length-2"
        namespace = "NISTSchema-SV-IV-list-date-length-2-NS"

    value: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )
