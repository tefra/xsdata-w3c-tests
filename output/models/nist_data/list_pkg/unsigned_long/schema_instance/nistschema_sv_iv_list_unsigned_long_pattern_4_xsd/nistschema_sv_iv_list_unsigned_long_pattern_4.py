from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedLong-pattern-4-NS"


@dataclass
class NistschemaSvIvListUnsignedLongPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedLong-pattern-4"
        namespace = "NISTSchema-SV-IV-list-unsignedLong-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1} \d{4} \d{7} \d{10} \d{13} \d{18}",
            "tokens": True,
        },
    )
