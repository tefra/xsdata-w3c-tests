from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-pattern-5-NS"


@dataclass
class NistschemaSvIvListQnamePattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-pattern-5"
        namespace = "NISTSchema-SV-IV-list-QName-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{29} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{34} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{49} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{37} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{21} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{14}",
            "tokens": True,
        },
    )
