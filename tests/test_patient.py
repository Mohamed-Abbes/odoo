from odoo.tests.common import TransactionCase
class TestBook(TransactionCase):
    def setUp(self,*args,**kwargs):
        super().setUp(*args,**kwargs)
        self.Patient = self.env["hospital.patient"]
        self.patient1=self.Patient.create({
            "name":"testpatient",
            "age":20,
        })
    def test_patient_create(self):
        self.assertEqual(
            self.patient1.active, True
        )
