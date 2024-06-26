from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-whiteSpace-2-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringWhiteSpace2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-whiteSpace-2"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-whiteSpace-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "collapse",
        },
    )
