from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-minLength-1-NS"


@dataclass
class NistschemaSvIvListGDayMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-minLength-1"
        namespace = "NISTSchema-SV-IV-list-gDay-minLength-1-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        },
    )
