from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Period

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-maxLength-5-NS"


@dataclass
class NistschemaSvIvListGDayMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-gDay-maxLength-5-NS"

    value: List[Period] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 10,
            "tokens": True,
        }
    )
