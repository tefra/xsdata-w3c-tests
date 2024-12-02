from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-short-maxLength-4-NS"


@dataclass
class NistschemaSvIvListShortMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-short-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-short-maxLength-4-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "max_length": 8,
            "tokens": True,
        },
    )
