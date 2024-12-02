from dataclasses import dataclass, field


@dataclass
class T:
    adam_com_eve_com_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://adam.com/ http://eve.com/",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class Eden(T):
    class Meta:
        name = "eden"
