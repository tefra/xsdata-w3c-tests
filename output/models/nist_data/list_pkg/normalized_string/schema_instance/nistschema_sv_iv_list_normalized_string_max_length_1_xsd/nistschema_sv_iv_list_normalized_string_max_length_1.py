from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-maxLength-1-NS"


@dataclass
class NistschemaSvIvListNormalizedStringMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-normalizedString-maxLength-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        },
    )
