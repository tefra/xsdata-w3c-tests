from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicQnamePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-QName-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{33}",
        },
    )
