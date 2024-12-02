from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-minLength-5-NS"


@dataclass
class NistschemaSvIvListGDayMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-minLength-5"
        namespace = "NISTSchema-SV-IV-list-gDay-minLength-5-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "min_length": 10,
            "tokens": True,
        },
    )
