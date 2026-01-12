import datetime


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError()
        if visitor["vaccine"] < datetime.date.today():
            raise OutdatedVaccineError()
        if visitor["wearing_a_mask"] is False or "wearing_a_mask" not in visitor:
            raise NotWearingMaskError()
        return f"Welcome to {self.name}"
