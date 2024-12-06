from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-maxLength-4-NS"


@dataclass
class NistschemaSvIvListGMonthDayMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-maxLength-4-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "max_length": 8,
            "tokens": True,
        },
    )
