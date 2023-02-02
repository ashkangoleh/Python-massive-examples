import asyncio
from curses import echo
import json
from box import Box
from sqlalchemy.sql.expression import literal
import yaml
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, Table, MetaData, VARCHAR, Column as c
from contextlib import asynccontextmanager
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
Base = declarative_base()
config = Box.from_yaml(
    filename="/external/test_proj/_SQLALCHEMY_TUT/db/config.yaml", Loader=yaml.FullLoader)

conf = config.database
username = conf.username
password = conf.password
url = conf.url
port = conf.port
db_name = conf.db_name


def engine():
    engine = create_async_engine(
        f"postgresql+asyncpg://{username}:{password}@{url}:{port}/{db_name}", echo=False, future=True, enable_from_linting=False)

    
    engine.sync_engine.dispose()
    return engine


meta = MetaData(bind=engine)
# meta.create_all(engine)


class Cites(Base):
    __tablename__ = 'cites'
    meta
    citing_paper_id = c(VARCHAR, primary_key=True)
    cited_paper_id = c(VARCHAR)

    @hybrid_property
    def x(self):
        return str(self.citing_paper_id) + " " + str(self.cited_paper_id)


class Content(Base):
    __tablename__ = 'content'
    meta
    paper_id = c(VARCHAR, primary_key=True)
    word_cited_id = c(VARCHAR)


AsyncLocalSession = sessionmaker(
    bind=engine(), expire_on_commit=False, class_=AsyncSession)


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
    stmt = select(Cites)
    result = await async_session.execute(stmt)
    return result.scalars().all()


@async_session
async def fetch_by_id(async_session):
    stmt = select(Cites).filter(Cites.cited_paper_id == 100157)
    result = await async_session.execute(stmt)
    return result.scalars().all()


@async_session
async def fetch_join(async_session):
    stmt = select(Cites, Content).join(
        Content, Cites.cited_paper_id == Content.paper_id).limit(10)
    result = await async_session.execute(stmt)
    return result.all()


@async_session
async def cross_join(async_session):
    stmt = select(Cites, Content).limit(10)
    result = await async_session.execute(stmt)

    return result.first()




@async_run
async def _fetch_id(l=fetch_id()):
    get_data = await l
    data = {}
    for i in get_data:
        data.setdefault(i.cited_paper_id, [])
        data[i.cited_paper_id].append(f"{i.citing_paper_id}")
    return json.dumps(data)


@async_run
async def _fetch_by_id(l=fetch_by_id()):
    data = await l
    return data


@async_run
async def _cross_join(l=cross_join()):
    data = await l
    return data


@async_run
async def _fetch_join(l=fetch_join()):
    get_data = await l
    data = {}
    for i in get_data:
        data.setdefault(f"{i[1].paper_id}", [])
        data[f"{i[1].paper_id}"].append(
            f"{i[0].citing_paper_id},{i[1].word_cited_id}")
    return json.dumps(data, indent=4)


# print("==>> _fetch_id: ", _fetch_id())
# print("==>> _fetch_join: ", _fetch_join())
# print("==>> _fetch_by_id: ", _fetch_by_id().x)
# print("==>> _cross_join: ", _cross_join())
_id = _fetch_by_id()
data ={}
for i in _id:
    data.setdefault(i.cited_paper_id, [])
    data[i.cited_paper_id].append(f"{i.citing_paper_id}")


df = pd.DataFrame(data)
print("==>> df: ", df.columns)
df.rename(columns={100157:"test"},inplace=True,index=str)
# df.set_index("test",inplace=True)
df.drop_duplicates(inplace=True)
print("==>> df: ", df)