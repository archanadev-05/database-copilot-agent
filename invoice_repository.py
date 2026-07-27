from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db_models import Invoice
from resp_models import InvoiceCreate


class InvoiceRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, invoice_create: InvoiceCreate) -> Invoice:
        invoice = Invoice(
            user_id=invoice_create.user_id,
            amount=invoice_create.amount,
            description=invoice_create.description,
        )

        self.db.add(invoice)
        await self.db.commit()
        await self.db.refresh(invoice)
        return invoice


    async def get_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        query = select(Invoice).where(Invoice.id == invoice_id)
        result = await self.db.execute(query)
        return result.scalars().first()


    async def get_invoices_by_user_id(
            self,
            user_id: int,
            skip: int = 0,
            limit: int = 10,
    ) -> list[Invoice]:
        query = (
            select(Invoice)
            .where(Invoice.user_id == user_id)
            .offset(skip)
            .limit(limit)
        )
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_all_invoices(
            self,
            skip: int = 0,
            limit: int = 10,
    ) -> list[Invoice]:
        query = select(Invoice).offset(skip).limit(limit)
        result = await self.db.execute(query)
        return result.scalars().all()