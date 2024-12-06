from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-maxLength-4-NS"


@dataclass
class NistschemaSvIvListDateMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-date-maxLength-4-NS"

    value: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "max_length": 8,
            "tokens": True,
        },
    )
