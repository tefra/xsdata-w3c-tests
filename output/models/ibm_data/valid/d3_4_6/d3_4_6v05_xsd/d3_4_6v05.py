from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass
class Nametest:
    ele: list[str] = field(
        default_factory=list,
        metadata={
            "name": "_ele",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        },
    )
    low_line_hyphen_minus: list[str] = field(
        default_factory=list,
        metadata={
            "name": "_-",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        },
    )
    low_line_full_stop: list[str] = field(
        default_factory=list,
        metadata={
            "name": "_.",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        },
    )
    value_9: list[str] = field(
        default_factory=list,
        metadata={
            "name": "_9",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        },
    )
    low_line_low_line_low_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "___",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        },
    )
    a_a: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        },
    )
    a_a_a: list[str] = field(
        default_factory=list,
        metadata={
            "name": "a.a",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        },
    )
    a_ele: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ele",
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        },
    )


@dataclass
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
