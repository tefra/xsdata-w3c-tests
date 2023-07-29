from output.models.ms_data.schema.sch_d5_a_xsd.ns_a import AE2
from output.models.ms_data.schema.sch_d5_a_xsd.ns_a import AE3
from output.models.ms_data.schema.sch_d5_a_xsd.ns_a import BE1
from output.models.ms_data.schema.sch_d5_a_xsd.ns_a import BE3
from output.models.ms_data.schema.sch_d5_a_xsd.ns_a import CE1
from output.models.ms_data.schema.sch_d5_a_xsd.ns_a import CE2
from output.models.ms_data.schema.sch_d5_a_xsd.ns_a import E1
from output.models.ms_data.schema.sch_d5_a_xsd.ns_a import E2
from output.models.ms_data.schema.sch_d5_a_xsd.ns_a import E3
from output.models.ms_data.schema.sch_d5_a_xsd.ns_a import Root


obj = Root(
    any_element=[
        E1(
            a1=123,
            a2=True
        ),
        E2(
            b1=True,
            b2=123
        ),
        E3(
            c1=123,
            c2=123
        ),
        E1(
            a1=123,
            a2=True
        ),
        AE2(
            b1=True,
            b2=123
        ),
        AE3(
            c1=123,
            c2=123
        ),
        BE1(
            a1=123,
            a2=True
        ),
        AE2(
            b1=True,
            b2=123
        ),
        BE3(
            c1=123,
            c2=123
        ),
        CE1(
            a1=123,
            a2=True
        ),
        CE2(
            b1=True,
            b2=123
        ),
        E3(
            c1=123,
            c2=123
        ),
    ]
)
