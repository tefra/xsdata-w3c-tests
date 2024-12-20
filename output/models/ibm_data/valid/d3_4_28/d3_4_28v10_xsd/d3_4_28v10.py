from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v10"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v10"

    d_time_stamp_pattern: list[str] = field(
        default_factory=list,
        metadata={
            "name": "dTimeStampPattern",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[1-2][0][0][0-9][-][0-1][1-2][-][0-3][1-8][T]*.*",
        },
    )
