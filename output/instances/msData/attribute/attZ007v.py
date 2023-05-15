from output.models.ms_data.attribute.att_z007_xsd.att_z007 import Doc
from output.models.ms_data.attribute.att_z007_xsd.att_z007 import One
from output.models.ms_data.attribute.att_z007_xsd.att_z007 import Three
from output.models.ms_data.attribute.att_z007_xsd.att_z007 import Two


obj = Doc(
    e1=One(
        att1="abc"
    ),
    e2=Two(

    ),
    e3=Three(
        att1="abc"
    )
)
