from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    and_,
    create_engine,
    MetaData,
    func,
    Table,
    VARCHAR,
    Column as c,
    alias,
    select,
    update,
    or_,
    and_
)
from sqlalchemy.sql import func
from box import Box
import yaml
from sqlalchemy.dialects.postgresql import insert as pg_insert

config = Box.from_yaml(
    filename="/external/test_proj/_SQLALCHEMY_TUT/db/config.yaml", Loader=yaml.FullLoader)

conf = config.database
username = conf.username
password = conf.password
url = conf.url
port = conf.port
db_name = conf.db_name

Base = declarative_base()

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{url}:{port}/{db_name}", pool_recycle=3600,  pool_size=40, max_overflow=0)
engine.execution_options(stream_results=True)
connection = engine.connect()
# Base = automap_base()
# Base.prepare(engine, reflect=True)
meta = MetaData(bind=connection)
meta.reflect(views=True)


# meta.create_all(connection)
cites = Table('cites', meta, autoload=True,
              extend_existing=True, autoload_with=connection)
content = Table('content', meta, autoload=True,
                extend_existing=True, autoload_with=connection)
paper = Table('paper', meta, autoload=True,
              extend_existing=True, autoload_with=connection)
cities = Table('cities', meta, autoload=True,
               extend_existing=True, autoload_with=connection)

# content = meta.tables['content']
# paper = meta.tables['paper']


session = sessionmaker(autocommit=False, autoflush=False, bind=connection)()


# ***********************************************SUBQUERY**************************************************
cites_sub = session.query(cites.c.cited_paper_id).filter(
    cites.c.cited_paper_id == 100157).scalar_subquery()
subquery = session.query(content).filter(content.c.paper_id.in_(cites_sub))

print(f"\033[92m subquery(result):{subquery.first()}\033[0m")
print(
    f"\033[94m subquery:{subquery.statement.compile(dialect=postgresql.dialect())}\033[0m")

# ***********************************************join**************************************************
cites_join = session.query(cites).join(content, cites.c.cited_paper_id ==
                                       content.c.paper_id).filter(cites.c.cited_paper_id == content.c.paper_id).limit(10)

print(f"\033[92m cites_join(result):{cites_join.all()}\033[0m")
print(
    f"\033[34m cites_join:{cites_join.statement.compile(dialect=postgresql.dialect())}\033[0m")

# ***********************************************outer join**************************************************
cites_join_outer = session.query(cites.c.cited_paper_id.label("id"), content.c.paper_id.label("cid")).join(
    content, content.c.paper_id == cites.c.cited_paper_id, isouter=True).filter(content.c.paper_id == cites.c.cited_paper_id)

print(f"\033[92m cites_join_outer(result):{cites_join_outer.first()}\033[0m")
print(
    f"\033[34m cites_join_outer:{cites_join_outer.statement.compile(dialect=postgresql.dialect())}\033[0m")


# ***********************************************getAttr**************************************************
cites_attr = session.query(getattr(cites.columns, "cited_paper_id").label("cited"), func.upper(getattr(
    cites.columns, "citing_paper_id")).label("citing")).order_by(cites.c.citing_paper_id.desc()).limit(10)
print(f"\033[92m cites_attr(result):{cites_attr.first()}\033[0m")
print(
    f"\033[34m cites_attr:{cites_attr.statement.compile(dialect=postgresql.dialect())}\033[0m")

# ***********************************************custom column**************************************************
cites_custom_col = session.query(cites.c.cited_paper_id).order_by(
    cites.c.citing_paper_id.desc()).limit(10)
print(f"\033[92m cites_custom_col(result):{cites_custom_col.first()}\033[0m")
print(
    f"\033[34m cites_custom_col:{cites_custom_col.statement.compile(dialect=postgresql.dialect())}\033[0m")

# ***********************************************select_entity_from**************************************************
select_smt = session.query(content).filter(
    content.c.paper_id == cites.c.cited_paper_id).scalar_subquery()
alias_smt = aliased(content, select_smt)
select_from_ = session.query(cites.c.citing_paper_id, alias_smt.c.word_cited_id).select_entity_from(
    alias_smt).filter(alias_smt.c.paper_id == cites.c.cited_paper_id)
print(f"\033[92m select_from_(result):{select_from_.first()}\033[0m")
print(
    f"\033[34m select_from_:{select_from_.statement.compile(dialect=postgresql.dialect())}\033[0m")
# ***********************************************with_for_update with metadata************************************

with_for_update = session.query(cites).filter(cites.c.cited_paper_id == 100157)
ww = with_for_update.with_for_update().update({
    "citing_paper_id": 12
})

print(f"\033[92m with_for_update(result):{ww}\033[0m")
print(
    f"\033[34m with_for_update:{ww}\033[0m")
session.commit()
# ***********************************************update_existing_table_by_MetaData************************************
update_param = "10000"
with_for_update = cites.update().where(cites.c.cited_paper_id ==
                                       100598).values(citing_paper_id=update_param)
print(
    f"\033[92m with_for_update(result): update parameter {update_param}\033[0m")
print(
    f"\033[34m with_for_update:{with_for_update}\033[0m")
session.execute(with_for_update)
session.commit()

# ***********************************************insert into reflected database************************************
ss = cites.insert().values(
    {"cited_paper_id": 9, "citing_paper_id": "asdfasdf12"})
session.execute(ss)
session.commit()

# ***********************************************having************************************

having_ = session.query(cites.c.cited_paper_id).group_by(
    cites.c.cited_paper_id).having(func.count(cites.c.cited_paper_id) > 1)
print(f"\033[92m having_(result):{having_.all().__len__()}\033[0m")
print(
    f"\033[34m having_:{having_.statement.compile(dialect=postgresql.dialect())}\033[0m")


# # ***********************************************insert by orm ************************************
class Cites(Base):
    __tablename__ = 'cites'
    meta
    citing_paper_id = c(VARCHAR, primary_key=True)
    cited_paper_id = c(VARCHAR)


cc = Cites(cited_paper_id=100000, citing_paper_id=200)

session.add(cc)
session.commit()
# ***********************************************insert on conflict by orm ************************************
# from sqlalchemy.dialects.postgresql import insert as pg_insert
# for i in range(100):
#     statement= pg_insert(cities).values({
#         "name":f"ashkan-{i}",
#     }).on_conflict_do_nothing(index_elements=['id'])

#     result = session.execute(statement)
# session.commit()
# print("==>> result.is_insert: ", result.is_insert)

# statement= pg_insert(cities).values({
#     "name":"ashkan-0"
# }).on_conflict_do_update(index_elements=['id'],set_= dict(name="1-11"))

# ***********************************************update orm on reflected database************************************
stmt = session.query(cites).filter(cites.c.citing_paper_id == "455651").update(
    {"citing_paper_id": "********************"})

print(f"\033[92m stmt(result): update parameter {str(stmt)}\033[0m")

session.commit()

# ***********************************************insert/update orm on conflict reflected database************************************
stmts = update(cities).where(cities.c.name == "spongebob").values(
    name="spongebob11").returning(cities.c.id)

for row in session.execute(stmts):
    print(f"\033[34m id: {row.id}\033[0m")
print(f"\033[92m stmts(result): update parameter {str(stmt)}\033[0m")


stmtts = pg_insert(cities).values(
    [
        dict(name="sandy"),
        dict(name="squidward"),
        dict(name="spongebob"),
    ]
)

stmtts = stmtts.on_conflict_do_update(
    index_elements=['id'], set_=dict(name=stmtts.excluded.name)
).returning(cities)

for user in session.execute(
    stmtts,
).scalars():
    print("\033[92m inserted or updated: %s\033[0m" % user)
session.commit()


# ***********************************************like in orm************************************


regx_stmt1 = session.query(cites).filter(cites.c.citing_paper_id.ilike(
    "windhouwer01flexible"))  # ilike means i contain
regx_stmt2 = session.query(cites).filter(
    cites.c.citing_paper_id.startswith("wi"))
regx_stmt3 = session.query(cites).filter(or_(cites.c.citing_paper_id.endswith(
    "ated"), cites.c.citing_paper_id.startswith("wi")))
regx_stmt4 = session.query(cites).filter(and_(
    cites.c.citing_paper_id.endswith("d"), cites.c.citing_paper_id.startswith("wi")))
print(f"\033[92m regx_stmt1(result): {str(regx_stmt1.all())}\033[0m")
print(f"\033[34mregx_stmt1(result): {str(regx_stmt1)}\033[0m")
print(f"\033[92m regx_stmt2(result): {str(regx_stmt2.all())}\033[0m")
print(f"\033[34mregx_stmt2(result): {str(regx_stmt2)}\033[0m")
print(f"\033[92m regx_stmt3(result): {str(regx_stmt3.all())}\033[0m")
print(f"\033[34mregx_stmt3(result): {str(regx_stmt3)}\033[0m")
print(f"\033[92m regx_stmt4(result): {str(regx_stmt4.all())}\033[0m")
print(f"\033[34mregx_stmt4(result): {str(regx_stmt4)}\033[0m")


# ***********************************************func and over************************************
over_func = session.query(func.count(content.c.paper_id).over(partition_by=content.c.word_cited_id),
                          content.c.paper_id, content.c.word_cited_id).filter(and_(content.c.paper_id == 32521, content.c.word_cited_id == "word1"))

print(f"\033[92m over_func(result): {str(over_func.all())}\033[0m")
print(f"\033[34m over_func(result): {str(over_func)}\033[0m")
