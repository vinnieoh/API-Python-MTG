from config.config_api import settings
from config.database import engine

import asyncio


async def create_tables() -> None:
    import models.__all_models

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
        
    print('Tabelas criadas!')


if __name__ == '__main__':
    asyncio.run(create_tables())