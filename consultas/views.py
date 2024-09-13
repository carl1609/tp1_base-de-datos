from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.

def index(request):
    return render(request,'base.html')

def evaluar_consultas(request,consulta):
    consultas={
        # Consultas para obtener objetos del servidor
        "consulta1": "SELECT datname FROM pg_database WHERE datallowconn=true;",
        "consulta2": "SELECT rolname FROM pg_roles WHERE rolcanlogin = true;",
        "consulta3": "SELECT groname FROM pg_group;",
        "consulta4": "SELECT lanname FROM pg_language;",

        # Consultas para obtener objetos de la base de datos
        "consulta5": "SELECT nspname FROM pg_namespace;",
        "consulta6": "SELECT tablename FROM pg_tables WHERE schemaname = 'public';",
        "consulta7": "SELECT table_name FROM information_schema.views WHERE table_schema NOT IN ('information_schema', 'pg_catalog');",
        "consulta8": "SELECT specific_name, routine_type FROM information_schema.routines WHERE routine_type = 'FUNCTION';",
        "consulta9": "SELECT tgname, tgrelid::regclass AS table_name, tgenabled, tgtype FROM pg_trigger;",
        "consulta10": "SELECT sequence_name FROM information_schema.sequences;",
        "consulta11": "SELECT schemaname, tablename, rulename, definition FROM pg_rules;",
        "consulta12": "SELECT typname FROM pg_type WHERE typtype = 'b' OR typtype = 'e' OR typtype = 'p' OR typtype = 'c' ORDER BY typname;",
        "consulta13": "SELECT indexname, indexdef FROM pg_indexes WHERE schemaname = 'public';",

        # Consultas para obtener detalles de los objetos
        "consulta14": "SELECT n.nspname AS schema_name, r.rolname AS role_name, has_schema_privilege(r.rolname, n.nspname, 'USAGE') AS usage_privilege, has_schema_privilege(r.rolname, n.nspname, 'CREATE') AS create_privilege FROM pg_namespace n CROSS JOIN pg_roles r WHERE n.nspname = 'nombre_del_esquema'; -- Reemplaza 'nombre_del_esquema' con el esquema que deseas consultar",
        "consulta15": "SELECT table_schema, table_name, ordinal_position, column_name, data_type FROM information_schema.columns WHERE table_schema = 'public';",
        "consulta16": "SELECT tc.table_schema, tc.table_name, kcu.column_name FROM information_schema.table_constraints AS tc JOIN information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_schema = 'public';",
        "consulta17": "SELECT tc.table_schema, tc.table_name, kcu.column_name, kcu.constraint_name FROM information_schema.table_constraints AS tc JOIN information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_schema = 'public';",
        "consulta18": "SELECT n.nspname AS schema_name, c.relname AS sequence_name, s.seqstart AS start_value, s.seqincrement AS increment_by, s.seqmax AS max_value, s.seqmin AS min_value, s.seqcache AS cache_size, CASE WHEN s.seqcycle THEN 'YES' ELSE 'NO' END AS is_cycled FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace JOIN pg_sequence s ON s.seqrelid = c.oid WHERE c.relkind = 'S' -- 'S' para secuencias AND n.nspname = 'nombre_del_esquema'; -- Reemplaza 'nombre_del_esquema' con el esquema que deseas consultar",
        "consulta19": "SELECT schemaname, tablename, indexname, indexdef FROM pg_indexes WHERE schemaname = 'public';",

        # Consultas para obtener detalles de privilegios de los objetos
        "consulta20": "SELECT grantee, privilege_type, is_grantable FROM information_schema.table_privileges WHERE table_schema = 'pg_catalog' AND table_name = 'pg_class';",
        "consulta21": "SELECT grantee, privilege_type, is_grantable FROM information_schema.routine_privileges WHERE specific_schema = 'pg_catalog' AND routine_name = 'pg_stat_get_activity';",

        # Consultas para monitoreo
        "consulta22": "SELECT pid, usename, client_addr, query FROM pg_stat_activity;",
        "consulta23": "SELECT datname AS database_name, pg_size_pretty(pg_database_size(datname)) AS size FROM pg_database;",
        "consulta24": "SELECT pg_size_pretty(pg_total_relation_size('apellidos_pais')) AS total_size",
        "consulta25": "SELECT table_name, pg_size_pretty(pg_total_relation_size(quote_ident(table_schema) || '.' || quote_ident(table_name))) AS size FROM information_schema.tables WHERE table_schema = 'public';",
        "consulta26": "SELECT current_database() AS database_name, schemaname AS schema_name, tablename AS table_name, pg_size_pretty(pg_total_relation_size(schemaname || '.' || tablename)) AS total_size, pg_size_pretty(pg_relation_size(schemaname || '.' || tablename)) AS table_size, pg_size_pretty(pg_indexes_size(schemaname || '.' || tablename)) AS index_size FROM pg_tables;"
    }

    #funcion para obtener la consulta me devuelve una lista de duplas con los resultados
    def obtener_consulta(consulta):
        with connection.cursor() as cursor:
            cursor.execute(consultas[consulta])
            resultado=cursor.fetchall()
            nombre_columnas=[desc[0] for desc in cursor.description]

        return resultado,nombre_columnas
    
    resultado,nombre_columnas=obtener_consulta(consulta)

    return render(request,'resultado.html',{'resultados':resultado,'columnas':nombre_columnas})




 