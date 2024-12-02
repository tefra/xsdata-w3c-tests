from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-byte-minLength-3-NS"


@dataclass
class NistschemaSvIvListByteMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-byte-minLength-3"
        namespace = "NISTSchema-SV-IV-list-byte-minLength-3-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "min_length": 7,
            "tokens": True,
        },
    )
