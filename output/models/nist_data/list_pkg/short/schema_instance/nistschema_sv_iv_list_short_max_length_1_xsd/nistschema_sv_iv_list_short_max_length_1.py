from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-short-maxLength-1-NS"


@dataclass
class NistschemaSvIvListShortMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-short-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-short-maxLength-1-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        },
    )
