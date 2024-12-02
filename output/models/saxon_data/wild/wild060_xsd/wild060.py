from dataclasses import dataclass, field


@dataclass
class Zing1:
    class Meta:
        name = "zing"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class ExtendedZing(Zing1):
    class Meta:
        name = "extendedZing"

    local_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )


@dataclass
class Zing(ExtendedZing):
    class Meta:
        name = "zing"
