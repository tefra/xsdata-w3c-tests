from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11"

    ele: list[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_length": 6,
            "format": "base64",
        },
    )
