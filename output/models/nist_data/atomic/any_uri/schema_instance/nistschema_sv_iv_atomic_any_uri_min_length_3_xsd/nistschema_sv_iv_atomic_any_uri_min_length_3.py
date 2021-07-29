from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-minLength-3-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-minLength-3"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-minLength-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 36,
        }
    )
