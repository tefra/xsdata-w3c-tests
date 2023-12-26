from output.models.ms_data.schema.sch_t3_a_xsd.sch_t3_a import E1
from output.models.ms_data.schema.sch_t3_a_xsd.sch_t3_a import E2
from output.models.ms_data.schema.sch_t3_a_xsd.sch_t3_a import Root
from output.models.ms_data.schema.sch_t3_a_xsd.sch_t3_b import BE1


obj = Root(
    any_element=[
        E1(
            att1='123',
            att3='123',
            att5='123',
            att6='true',
            att7='123',
            att9='123',
            att11=1,
            att12='true',
            att14='true'
        ),
        BE1(
            att1='123',
            att3='123',
            att5='123',
            att6='true',
            att7='123',
            att9='123',
            att11=1,
            att12='true',
            att14='true'
        ),
        E2(
            value=12
        ),
    ]
)
