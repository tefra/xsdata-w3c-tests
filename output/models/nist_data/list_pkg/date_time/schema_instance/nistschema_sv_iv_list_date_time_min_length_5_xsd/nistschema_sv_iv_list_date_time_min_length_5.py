from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-minLength-5-NS"


@dataclass
class NistschemaSvIvListDateTimeMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-minLength-5"
        namespace = "NISTSchema-SV-IV-list-dateTime-minLength-5-NS"

    value: list[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "min_length": 10,
            "tokens": True,
        },
    )
