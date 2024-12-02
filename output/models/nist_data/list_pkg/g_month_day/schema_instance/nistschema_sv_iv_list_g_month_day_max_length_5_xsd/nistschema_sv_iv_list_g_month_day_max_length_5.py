from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-maxLength-5-NS"


@dataclass
class NistschemaSvIvListGMonthDayMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-maxLength-5-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
        },
    )
