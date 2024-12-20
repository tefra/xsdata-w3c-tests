from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-pattern-4-NS"


@dataclass
class NistschemaSvIvListQnamePattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-pattern-4"
        namespace = "NISTSchema-SV-IV-list-QName-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{9} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{35} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{50} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{15} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{27} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{18} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{26}",
            "tokens": True,
        },
    )
