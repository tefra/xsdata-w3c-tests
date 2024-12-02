from dataclasses import dataclass, field

__NAMESPACE__ = "nsConstraint"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    ns_test1_ns_test2_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "ns_test1 ns_test2",
        },
    )
