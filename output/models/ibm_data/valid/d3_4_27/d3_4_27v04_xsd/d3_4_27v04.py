from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v04"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v04"

    ely_mdmin_inclusive_min_inclusive: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MinInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": XmlDuration("P1DT535.4S"),
        },
    )
    ely_mdmin_inclusive_min_exclusive: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MinExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": XmlDuration("P2D"),
            "min_inclusive": XmlDuration("P1D"),
        },
    )
    ely_mdmin_inclusive_max_inclusive: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": XmlDuration("P1D"),
            "max_inclusive": XmlDuration("P3452DT2H"),
        },
    )
    ely_mdmin_inclusive_max_exclusive: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": XmlDuration("P1D"),
            "max_exclusive": XmlDuration("P43DT43M"),
        },
    )
