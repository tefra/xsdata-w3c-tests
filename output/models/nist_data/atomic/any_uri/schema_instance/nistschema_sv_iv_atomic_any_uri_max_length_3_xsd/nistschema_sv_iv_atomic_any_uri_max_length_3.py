from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-maxLength-3-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-maxLength-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 26,
        }
    )
