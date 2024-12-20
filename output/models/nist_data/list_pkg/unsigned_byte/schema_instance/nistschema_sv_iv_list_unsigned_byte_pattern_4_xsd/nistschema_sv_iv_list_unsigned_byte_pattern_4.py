from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-pattern-4-NS"


@dataclass
class NistschemaSvIvListUnsignedBytePattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-pattern-4"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1} \d{2} \d{3} \d{1} \d{2} \d{3} \d{1} \d{2} \d{3}",
            "tokens": True,
        },
    )
