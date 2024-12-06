from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-byte-minLength-1-NS"


@dataclass
class NistschemaSvIvListByteMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-byte-minLength-1"
        namespace = "NISTSchema-SV-IV-list-byte-minLength-1-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        },
    )
