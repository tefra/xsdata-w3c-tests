from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-length-3-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-length-3"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-length-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 916,
        },
    )
