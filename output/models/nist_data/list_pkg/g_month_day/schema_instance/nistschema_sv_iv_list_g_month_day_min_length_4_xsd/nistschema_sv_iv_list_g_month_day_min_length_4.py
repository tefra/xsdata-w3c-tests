from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-minLength-4-NS"


@dataclass
class NistschemaSvIvListGMonthDayMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-minLength-4"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-minLength-4-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "min_length": 8,
            "tokens": True,
        },
    )
