from sqlmodel import SQLModel, Field,create_engine,Session,select,insert,update


engine = create_engine("postgresql+psycopg2://root:1@arz.local:5432/postgres", echo=True)
# SQLModel.metadata.create_all(engine)

class cites(SQLModel, table=True):
    cited_paper_id: str = Field(primary_key=True)
    citing_paper_id: str


with Session(engine) as session:
    in_ = cites(cited_paper_id=1212,citing_paper_id=1212)
    statement = select(cites.citing_paper_id).where(cites.cited_paper_id==1212)
    result = session.execute(statement).all()
    session.add(in_)
    session.commit()
    print("==>> result: ", result)
    
        
