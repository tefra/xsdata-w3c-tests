from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicQnamePattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-QName-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{27}",
        },
    )
