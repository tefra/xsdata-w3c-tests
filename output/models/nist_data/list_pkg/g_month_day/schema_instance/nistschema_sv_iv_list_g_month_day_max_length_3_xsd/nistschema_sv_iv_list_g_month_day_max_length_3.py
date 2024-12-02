from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-maxLength-3-NS"


@dataclass
class NistschemaSvIvListGMonthDayMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-maxLength-3-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "max_length": 7,
            "tokens": True,
        },
    )
