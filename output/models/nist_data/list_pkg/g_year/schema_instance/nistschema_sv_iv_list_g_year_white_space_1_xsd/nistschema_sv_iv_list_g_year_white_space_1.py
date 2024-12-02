from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListGYearWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-gYear-whiteSpace-1-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        },
    )
