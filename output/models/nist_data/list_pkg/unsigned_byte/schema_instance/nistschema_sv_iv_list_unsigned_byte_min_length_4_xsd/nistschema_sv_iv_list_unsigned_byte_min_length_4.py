from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-minLength-4-NS"


@dataclass
class NistschemaSvIvListUnsignedByteMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-minLength-4"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-minLength-4-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "min_length": 8,
            "tokens": True,
        },
    )
