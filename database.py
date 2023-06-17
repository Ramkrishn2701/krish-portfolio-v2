from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://8s70frx4jeuismncvjv5:pscale_pw_C9GvO6xe6pBsDlsR8NsdHAEqLhvvAixSlgLOQtY6X08@aws.connect.psdb.cloud/krish-portfolio-v2?charset=utf8mb4"

engine = create_engine(db_connection_string,
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
