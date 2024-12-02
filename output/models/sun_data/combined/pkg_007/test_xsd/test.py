from dataclasses import dataclass, field

__NAMESPACE__ = "urn:foo"


@dataclass
class Emptywc:
    class Meta:
        name = "emptywc"
        namespace = "urn:foo"

    a_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "urn:a",
        },
    )
    b_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "urn:b",
        },
    )


@dataclass
class JustA:
    class Meta:
        name = "justA"
        namespace = "urn:foo"

    a_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "urn:a",
        },
    )
    a_b_c_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "urn:a urn:b urn:c",
        },
    )
