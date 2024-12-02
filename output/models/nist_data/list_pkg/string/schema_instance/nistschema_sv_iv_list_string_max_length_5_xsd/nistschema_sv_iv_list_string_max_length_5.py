from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-maxLength-5-NS"


@dataclass
class NistschemaSvIvListStringMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-string-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-string-maxLength-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
        },
    )
