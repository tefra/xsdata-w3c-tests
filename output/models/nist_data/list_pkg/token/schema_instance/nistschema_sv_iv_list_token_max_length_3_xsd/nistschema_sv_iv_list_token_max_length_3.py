from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-maxLength-3-NS"


@dataclass
class NistschemaSvIvListTokenMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-token-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-token-maxLength-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "max_length": 7,
            "tokens": True,
        },
    )
