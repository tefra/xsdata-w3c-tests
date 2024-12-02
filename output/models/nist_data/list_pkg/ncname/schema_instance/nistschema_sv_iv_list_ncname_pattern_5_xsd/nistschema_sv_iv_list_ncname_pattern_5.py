from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NCName-pattern-5-NS"


@dataclass
class NistschemaSvIvListNcnamePattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-NCName-pattern-5"
        namespace = "NISTSchema-SV-IV-list-NCName-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[\i-[:]][\c-[:]]{40} [\i-[:]][\c-[:]]{59} [\i-[:]][\c-[:]]{55} [\i-[:]][\c-[:]]{41} [\i-[:]][\c-[:]]{12} [\i-[:]][\c-[:]]{25}",
            "tokens": True,
        },
    )
