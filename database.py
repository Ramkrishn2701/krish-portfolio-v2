from sqlalchemy import create_engine, text
import os

my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from portfolio"))
    result_all = result.all()
    column_names = result.keys()
    projects = []
    for row in result_all:
      projects.append(dict(zip(column_names, row)))
      print(projects)
    return projects


#   return projects
