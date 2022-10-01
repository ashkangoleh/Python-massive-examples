import asyncio
from curses import echo
from box import Box
import yaml
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, Table, MetaData, VARCHAR, Column as c
from contextlib import asynccontextmanager
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# config = Box.from_yaml(
#     filename="./config.yaml", Loader=yaml.FullLoader)
conf = "postgres"
username = "root"
password = 1
url = "arz.local"
port = 5432
db_name = "postgres"

engine = create_async_engine(
    f"postgresql+asyncpg://{username}:{password}@{url}:{port}/{db_name}", echo=False, future=True)

meta = MetaData(bind=engine)
# meta.create_all(engine)


class Cites(Base):
    __tablename__ = 'cites'
    meta
    citing_paper_id = c(VARCHAR, primary_key=True)
    cited_paper_id = c(VARCHAR)


AsyncLocalSession = sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession)


def async_run(coroutine):
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(coroutine(*args, **kwargs))
        finally:
            loop.close()
    return wrapper


@asynccontextmanager
async def get_async_session():
    session = AsyncLocalSession()
    try:
        yield session
    except Exception as e:
        print(e)
        await session.rollback()
    finally:
        await session.close()


def async_session(func):
    async def wrapper(*args, **kwargs):
        async with get_async_session() as session:
            return await func(session, *args, **kwargs)
    return wrapper



# @async_run
@async_session
async def fetch_id(async_session):
    stmt = select(Cites).filter_by(citing_paper_id="asdfasdf12")
    result = await async_session.execute(stmt)
    return result.scalars().all()


@async_run
async def test(l=fetch_id()):
    get_data  = await l
    data = {}
    dd = []
    for i in get_data:
        data.setdefault(i.cited_paper_id,[])
        data[i.cited_paper_id].append(f"{i.citing_paper_id}")
    print("==>> data: ", data)



test()