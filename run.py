import sys
import duckdb

input = sys.argv[1]

data = duckdb.sql(f"""
	SELECT * FROM read_csv('{input}',
		delim = ';',
		header = false,
		columns = {{'location': 'VARCHAR', 'temperature': 'REAL'}}
	);
""")

result = duckdb.sql("""select location, min(temperature), max(temperature), round(avg(temperature),1) from data group by location order by location""")
print(result)
