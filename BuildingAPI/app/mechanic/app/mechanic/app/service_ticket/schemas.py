from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import ServiceTicket


class ServiceTicketSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceTicket
        load_instance = True


ticket_schema = ServiceTicketSchema()
tickets_schema = ServiceTicketSchema(many=True)