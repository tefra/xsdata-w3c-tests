from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-minLength-2-NS"


@dataclass
class NistschemaSvIvListGMonthMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-minLength-2"
        namespace = "NISTSchema-SV-IV-list-gMonth-minLength-2-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "min_length": 6,
            "tokens": True,
        },
    )
