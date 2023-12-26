from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_D4_3_15"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D4_3_15"

    value: str = field(default="")
