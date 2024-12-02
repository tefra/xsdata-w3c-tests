from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/IBMd3_16v02"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/IBMd3_16v02"

    elflt_union_c: list[float] = field(
        default_factory=list,
        metadata={
            "name": "elfltUnionC",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": -12.0,
            "max_inclusive": 12.0,
        },
    )
