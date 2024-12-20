from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-length-3-NS"


@dataclass
class NistschemaSvIvListNormalizedStringLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-length-3"
        namespace = "NISTSchema-SV-IV-list-normalizedString-length-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
        },
    )
