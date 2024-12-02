from dataclasses import dataclass, field


@dataclass
class B:
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class R(B):
    pass


@dataclass
class Eden(R):
    class Meta:
        name = "eden"
