from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/IBMd3_16v04"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/IBMd3_16v04"

    union_element: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2-9][2-9]",
        },
    )
