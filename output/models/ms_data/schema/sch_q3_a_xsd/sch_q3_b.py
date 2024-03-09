from dataclasses import dataclass

from output.models.ms_data.schema.sch_q3_a_xsd.sch_q3_a import BCt

__NAMESPACE__ = "ns-a"


@dataclass
class BE1(BCt):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"
