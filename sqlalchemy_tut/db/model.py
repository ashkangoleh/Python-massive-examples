from sqlalchemy.ext.automap import automap_base
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import (
    create_engine,
    MetaData,
    func
)
from box import Box
import yaml

config = Box.from_yaml(
    filename="/external/test_proj/sqlalchemy_tut/db/config.yaml", Loader=yaml.FullLoader)
conf = config.database
username = conf.username
password = conf.password
url = conf.url
port = conf.port
db_name = conf.db_name

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{url}:{port}/{db_name}")
engine.execution_options(stream_results=True)
meta = MetaData(bind=engine)
meta.reflect(views=True)
# base = automap_base(bind=engine)
# base.prepare(engine, reflect=True)


cites = meta.tables['cites']
content = meta.tables['content']
paper = meta.tables['paper']

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()


# ***********************************************SUBQUERY**************************************************
cites_sub = session.query(cites.c.cited_paper_id).filter(
    cites.c.cited_paper_id == 100157).scalar_subquery()
subquery = session.query(content).filter(content.c.paper_id.in_(cites_sub))

print(f"\033[92m subquery(result):{subquery.first()}\033[0m")
print(
    f"\033[94m subquery:{subquery.statement.compile(dialect=postgresql.dialect())}\033[0m")

# ***********************************************join**************************************************
cites_join = session.query(cites).join(content, cites.c.cited_paper_id ==
                                       content.c.paper_id).filter(cites.c.cited_paper_id == content.c.paper_id)

print(f"\033[92m cites_join(result):{cites_join.first()}\033[0m")
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
select_smt = session.query(content).filter(content.c.paper_id==cites.c.cited_paper_id).scalar_subquery()
alias_smt = aliased(content,select_smt)
select_from_ = session.query(cites.c.citing_paper_id,alias_smt.c.word_cited_id).select_entity_from(alias_smt).filter(alias_smt.c.paper_id==cites.c.cited_paper_id)
print(f"\033[92m select_from_(result):{select_from_.first()}\033[0m")
print(
    f"\033[34m select_from_:{select_from_.statement.compile(dialect=postgresql.dialect())}\033[0m")


