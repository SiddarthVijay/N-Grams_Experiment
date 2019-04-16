from wtforms import Form, StringField, validators


class ChooseExperiment(Form):
    choice = StringField('Choose Between Corpus A & B', [
                         validators.Length(min=1, max=1)])


class ExperimentCorpusA(Form):
    field1_1 = StringField('', [validators.Length(min=1)])
    field1_2 = StringField('', [validators.Length(min=1)])
    field1_3 = StringField('', [validators.Length(min=1)])
    field1_4 = StringField('', [validators.Length(min=1)])
    field1_5 = StringField('', [validators.Length(min=1)])
    field1_6 = StringField('', [validators.Length(min=1)])
    field1_7 = StringField('', [validators.Length(min=1)])
    field2_1 = StringField('', [validators.Length(min=1)])
    field2_2 = StringField('', [validators.Length(min=1)])
    field2_3 = StringField('', [validators.Length(min=1)])
    field2_4 = StringField('', [validators.Length(min=1)])
    field2_5 = StringField('', [validators.Length(min=1)])
    field2_6 = StringField('', [validators.Length(min=1)])
    field2_7 = StringField('', [validators.Length(min=1)])
    field3_1 = StringField('', [validators.Length(min=1)])
    field3_2 = StringField('', [validators.Length(min=1)])
    field3_3 = StringField('', [validators.Length(min=1)])
    field3_4 = StringField('', [validators.Length(min=1)])
    field3_5 = StringField('', [validators.Length(min=1)])
    field3_6 = StringField('', [validators.Length(min=1)])
    field3_7 = StringField('', [validators.Length(min=1)])
    field4_1 = StringField('', [validators.Length(min=1)])
    field4_2 = StringField('', [validators.Length(min=1)])
    field4_3 = StringField('', [validators.Length(min=1)])
    field4_4 = StringField('', [validators.Length(min=1)])
    field4_5 = StringField('', [validators.Length(min=1)])
    field4_6 = StringField('', [validators.Length(min=1)])
    field4_7 = StringField('', [validators.Length(min=1)])
    field5_1 = StringField('', [validators.Length(min=1)])
    field5_2 = StringField('', [validators.Length(min=1)])
    field5_3 = StringField('', [validators.Length(min=1)])
    field5_4 = StringField('', [validators.Length(min=1)])
    field5_5 = StringField('', [validators.Length(min=1)])
    field5_6 = StringField('', [validators.Length(min=1)])
    field5_7 = StringField('', [validators.Length(min=1)])
    field6_1 = StringField('', [validators.Length(min=1)])
    field6_2 = StringField('', [validators.Length(min=1)])
    field6_3 = StringField('', [validators.Length(min=1)])
    field6_4 = StringField('', [validators.Length(min=1)])
    field6_5 = StringField('', [validators.Length(min=1)])
    field6_6 = StringField('', [validators.Length(min=1)])
    field6_7 = StringField('', [validators.Length(min=1)])
    field7_1 = StringField('', [validators.Length(min=1)])
    field7_2 = StringField('', [validators.Length(min=1)])
    field7_3 = StringField('', [validators.Length(min=1)])
    field7_4 = StringField('', [validators.Length(min=1)])
    field7_5 = StringField('', [validators.Length(min=1)])
    field7_6 = StringField('', [validators.Length(min=1)])
    field7_7 = StringField('', [validators.Length(min=1)])


class ExperimentCorpusB(Form):
    field1_1 = StringField('', [validators.Length(min=1)])
    field1_2 = StringField('', [validators.Length(min=1)])
    field1_3 = StringField('', [validators.Length(min=1)])
    field1_4 = StringField('', [validators.Length(min=1)])
    field1_5 = StringField('', [validators.Length(min=1)])
    field1_6 = StringField('', [validators.Length(min=1)])
    field1_7 = StringField('', [validators.Length(min=1)])
    field1_8 = StringField('', [validators.Length(min=1)])
    field1_9 = StringField('', [validators.Length(min=1)])
    field1_10 = StringField('', [validators.Length(min=1)])
    field1_11 = StringField('', [validators.Length(min=1)])
    field2_1 = StringField('', [validators.Length(min=1)])
    field2_2 = StringField('', [validators.Length(min=1)])
    field2_3 = StringField('', [validators.Length(min=1)])
    field2_4 = StringField('', [validators.Length(min=1)])
    field2_5 = StringField('', [validators.Length(min=1)])
    field2_6 = StringField('', [validators.Length(min=1)])
    field2_7 = StringField('', [validators.Length(min=1)])
    field2_8 = StringField('', [validators.Length(min=1)])
    field2_9 = StringField('', [validators.Length(min=1)])
    field2_10 = StringField('', [validators.Length(min=1)])
    field2_11 = StringField('', [validators.Length(min=1)])
    field3_1 = StringField('', [validators.Length(min=1)])
    field3_2 = StringField('', [validators.Length(min=1)])
    field3_3 = StringField('', [validators.Length(min=1)])
    field3_4 = StringField('', [validators.Length(min=1)])
    field3_5 = StringField('', [validators.Length(min=1)])
    field3_6 = StringField('', [validators.Length(min=1)])
    field3_7 = StringField('', [validators.Length(min=1)])
    field3_8 = StringField('', [validators.Length(min=1)])
    field3_9 = StringField('', [validators.Length(min=1)])
    field3_10 = StringField('', [validators.Length(min=1)])
    field3_11 = StringField('', [validators.Length(min=1)])
    field4_1 = StringField('', [validators.Length(min=1)])
    field4_2 = StringField('', [validators.Length(min=1)])
    field4_3 = StringField('', [validators.Length(min=1)])
    field4_4 = StringField('', [validators.Length(min=1)])
    field4_5 = StringField('', [validators.Length(min=1)])
    field4_6 = StringField('', [validators.Length(min=1)])
    field4_7 = StringField('', [validators.Length(min=1)])
    field4_8 = StringField('', [validators.Length(min=1)])
    field4_9 = StringField('', [validators.Length(min=1)])
    field4_10 = StringField('', [validators.Length(min=1)])
    field4_11 = StringField('', [validators.Length(min=1)])
    field5_1 = StringField('', [validators.Length(min=1)])
    field5_2 = StringField('', [validators.Length(min=1)])
    field5_3 = StringField('', [validators.Length(min=1)])
    field5_4 = StringField('', [validators.Length(min=1)])
    field5_5 = StringField('', [validators.Length(min=1)])
    field5_6 = StringField('', [validators.Length(min=1)])
    field5_7 = StringField('', [validators.Length(min=1)])
    field5_8 = StringField('', [validators.Length(min=1)])
    field5_9 = StringField('', [validators.Length(min=1)])
    field5_10 = StringField('', [validators.Length(min=1)])
    field5_11 = StringField('', [validators.Length(min=1)])
    field6_1 = StringField('', [validators.Length(min=1)])
    field6_2 = StringField('', [validators.Length(min=1)])
    field6_3 = StringField('', [validators.Length(min=1)])
    field6_4 = StringField('', [validators.Length(min=1)])
    field6_5 = StringField('', [validators.Length(min=1)])
    field6_6 = StringField('', [validators.Length(min=1)])
    field6_7 = StringField('', [validators.Length(min=1)])
    field6_8 = StringField('', [validators.Length(min=1)])
    field6_9 = StringField('', [validators.Length(min=1)])
    field6_10 = StringField('', [validators.Length(min=1)])
    field6_11 = StringField('', [validators.Length(min=1)])
    field7_1 = StringField('', [validators.Length(min=1)])
    field7_2 = StringField('', [validators.Length(min=1)])
    field7_3 = StringField('', [validators.Length(min=1)])
    field7_4 = StringField('', [validators.Length(min=1)])
    field7_5 = StringField('', [validators.Length(min=1)])
    field7_6 = StringField('', [validators.Length(min=1)])
    field7_7 = StringField('', [validators.Length(min=1)])
    field7_8 = StringField('', [validators.Length(min=1)])
    field7_9 = StringField('', [validators.Length(min=1)])
    field7_10 = StringField('', [validators.Length(min=1)])
    field7_11 = StringField('', [validators.Length(min=1)])
    field8_1 = StringField('', [validators.Length(min=1)])
    field8_2 = StringField('', [validators.Length(min=1)])
    field8_3 = StringField('', [validators.Length(min=1)])
    field8_4 = StringField('', [validators.Length(min=1)])
    field8_5 = StringField('', [validators.Length(min=1)])
    field8_6 = StringField('', [validators.Length(min=1)])
    field8_7 = StringField('', [validators.Length(min=1)])
    field8_8 = StringField('', [validators.Length(min=1)])
    field8_9 = StringField('', [validators.Length(min=1)])
    field8_10 = StringField('', [validators.Length(min=1)])
    field8_11 = StringField('', [validators.Length(min=1)])
    field9_1 = StringField('', [validators.Length(min=1)])
    field9_2 = StringField('', [validators.Length(min=1)])
    field9_3 = StringField('', [validators.Length(min=1)])
    field9_4 = StringField('', [validators.Length(min=1)])
    field9_5 = StringField('', [validators.Length(min=1)])
    field9_6 = StringField('', [validators.Length(min=1)])
    field9_7 = StringField('', [validators.Length(min=1)])
    field9_8 = StringField('', [validators.Length(min=1)])
    field9_9 = StringField('', [validators.Length(min=1)])
    field9_10 = StringField('', [validators.Length(min=1)])
    field9_11 = StringField('', [validators.Length(min=1)])
    field10_1 = StringField('', [validators.Length(min=1)])
    field10_2 = StringField('', [validators.Length(min=1)])
    field10_3 = StringField('', [validators.Length(min=1)])
    field10_4 = StringField('', [validators.Length(min=1)])
    field10_5 = StringField('', [validators.Length(min=1)])
    field10_6 = StringField('', [validators.Length(min=1)])
    field10_7 = StringField('', [validators.Length(min=1)])
    field10_8 = StringField('', [validators.Length(min=1)])
    field10_9 = StringField('', [validators.Length(min=1)])
    field10_10 = StringField('', [validators.Length(min=1)])
    field10_11 = StringField('', [validators.Length(min=1)])
    field11_1 = StringField('', [validators.Length(min=1)])
    field11_2 = StringField('', [validators.Length(min=1)])
    field11_3 = StringField('', [validators.Length(min=1)])
    field11_4 = StringField('', [validators.Length(min=1)])
    field11_5 = StringField('', [validators.Length(min=1)])
    field11_6 = StringField('', [validators.Length(min=1)])
    field11_7 = StringField('', [validators.Length(min=1)])
    field11_8 = StringField('', [validators.Length(min=1)])
    field11_9 = StringField('', [validators.Length(min=1)])
    field11_10 = StringField('', [validators.Length(min=1)])
    field11_11 = StringField('', [validators.Length(min=1)])
