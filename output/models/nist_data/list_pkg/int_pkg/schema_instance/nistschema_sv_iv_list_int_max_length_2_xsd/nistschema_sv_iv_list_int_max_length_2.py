from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-maxLength-2-NS"


@dataclass
class NistschemaSvIvListIntMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-int-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-int-maxLength-2-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "max_length": 6,
            "tokens": True,
        },
    )
