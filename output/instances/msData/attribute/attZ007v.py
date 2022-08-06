from output.models.ms_data.attribute.att_z007_xsd.att_z007 import Doc
from output.models.ms_data.attribute.att_z007_xsd.att_z007 import One
from output.models.ms_data.attribute.att_z007_xsd.att_z007 import Three
from output.models.ms_data.attribute.att_z007_xsd.att_z007 import Two


obj = Doc(
    e1=One(
        elem1=None,
        elem2=None,
        att1="abc",
        att2=None
    ),
    e2=Two(
        elem1=None,
        elem2=None,
        att1=None,
        att2=None
    ),
    e3=Three(
        elem1=None,
        elem2=None,
        att1="abc",
        att2=None
    )
)
