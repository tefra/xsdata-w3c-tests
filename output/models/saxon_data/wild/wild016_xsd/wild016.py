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
class E(B):
    abel_com_adam_com_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://abel.com/ http://adam.com/",
        },
    )


@dataclass
class Eden(E):
    class Meta:
        name = "eden"
