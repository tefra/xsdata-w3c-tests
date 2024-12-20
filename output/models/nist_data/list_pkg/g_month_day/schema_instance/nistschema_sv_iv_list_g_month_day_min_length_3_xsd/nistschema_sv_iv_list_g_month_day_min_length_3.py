from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-minLength-3-NS"


@dataclass
class NistschemaSvIvListGMonthDayMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-minLength-3"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-minLength-3-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "min_length": 7,
            "tokens": True,
        },
    )
