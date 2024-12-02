from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-length-2-NS"


@dataclass
class NistschemaSvIvListGYearLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-length-2"
        namespace = "NISTSchema-SV-IV-list-gYear-length-2-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )
