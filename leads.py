import models, schemas
from sqlalchemy.orm import Session


def leads_data(db: Session, leads_input: schemas.leadschema):
    lead_data = models.Leads(first_name=leads_input.first_name, last_name=leads_input.last_name, work_phone=leads_input.work_phone)
    db.add(lead_data)
    db.commit()
    db.refresh(lead_data)
    return lead_data
