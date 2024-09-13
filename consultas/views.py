from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.

def index(request):
    return render(request,'base.html')

def evaluar_consultas(request, consulta):

    consultas = {

        # Consultas para obtener objetos del servidor
        "bases-disponibles": "SELECT datname \nFROM pg_database \nWHERE datallowconn=true;",
        "roles": "SELECT rolname FROM pg_roles WHERE rolcanlogin = true;",
        "grupos-existentes": "SELECT groname FROM pg_group;",
        "lenguajes": "SELECT lanname FROM pg_language;",

        # Consultas para obtener objetos de la base de datos
        "bbdd-esquemas": "SELECT nspname FROM pg_namespace;",
        "bbdd-tablas-de-esquema": "SELECT tablename FROM pg_tables WHERE schemaname = 'public';",
        "bbdd-vistas": "SELECT table_name FROM information_schema.views WHERE table_schema NOT IN ('information_schema', 'pg_catalog');",
        "bbdd-funciones": "SELECT specific_name, routine_type FROM information_schema.routines WHERE routine_type = 'FUNCTION';",
        "bbdd-triggers": "SELECT tgname, tgrelid::regclass AS table_name, tgenabled, tgtype FROM pg_trigger;",
        "bbdd-secuencias": "SELECT sequence_name FROM information_schema.sequences;",
        "bbdd-reglas": "SELECT schemaname, tablename, rulename, definition FROM pg_rules;",
        "bbdd-datatypes": "SELECT typname FROM pg_type WHERE typtype = 'b' OR typtype = 'e' OR typtype = 'p' OR typtype = 'c' ORDER BY typname;",
        "bbdd-indices": "SELECT indexname, indexdef FROM pg_indexes WHERE schemaname = 'public';",

        # Consultas para obtener detalles de los objetos
        "esquemas-detalles": "SELECT n.nspname AS schema_name, r.rolname AS role_name, has_schema_privilege(r.rolname, n.nspname, 'USAGE') AS usage_privilege, has_schema_privilege(r.rolname, n.nspname, 'CREATE') AS create_privilege FROM pg_namespace n CROSS JOIN pg_roles r WHERE n.nspname = 'nombre_del_esquema'; -- Reemplaza 'nombre_del_esquema' con el esquema que deseas consultar",
        "tablas-detalles": "SELECT table_schema, table_name, ordinal_position, column_name, data_type FROM information_schema.columns WHERE table_schema = 'public';",
        "tablas-primarykey": "SELECT tc.table_schema, tc.table_name, kcu.column_name FROM information_schema.table_cgionstraints AS tc JOIN information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_schema = 'public';",
        "tablas-foreignkeys": "SELECT tc.table_schema, tc.table_name, kcu.column_name, kcu.constraint_name FROM information_schema.table_constraints AS tc JOIN information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_schema = 'public';",
        "secuencias-detalles": "SELECT n.nspname AS schema_name, c.relname AS sequence_name, s.seqstart AS start_value, s.seqincrement AS increment_by, s.seqmax AS max_value, s.seqmin AS min_value, s.seqcache AS cache_size, CASE WHEN s.seqcycle THEN 'YES' ELSE 'NO' END AS is_cycled FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace JOIN pg_sequence s ON s.seqrelid = c.oid WHERE c.relkind = 'S' -- 'S' para secuencias AND n.nspname = 'nombre_del_esquema'; -- Reemplaza 'nombre_del_esquema' con el esquema que deseas consultar",
        "indices-definicion": "SELECT schemaname, tablename, indexname, indexdef FROM pg_indexes WHERE schemaname = 'public';",

        # Consultas para obtener detalles de privilegios de los objetos
        "privilegios-tablas": "SELECT grantee, privilege_type, is_grantable FROM information_schema.table_privileges WHERE table_schema = 'pg_catalog' AND table_name = 'pg_class';",
        "privilegios-funciones": "SELECT grantee, privilege_type, is_grantable FROM information_schema.routine_privileges WHERE specific_schema = 'pg_catalog' AND routine_name = 'pg_stat_get_activity';",

        # Consultas para monitoreo
        "monitorear-conexiones": "SELECT pid, usename, client_addr, query FROM pg_stat_activity;",
        "tamanio-bbdd": "SELECT datname AS database_name, pg_size_pretty(pg_database_size(datname)) AS size FROM pg_database;",
        "tamanio-tablas": "SELECT pg_size_pretty(pg_total_relation_size('apellidos_pais')) AS total_size",
        "tamanio-tablas-esquema": "SELECT table_name, pg_size_pretty(pg_total_relation_size(quote_ident(table_schema) || '.' || quote_ident(table_name))) AS size FROM information_schema.tables WHERE table_schema = 'public';",
        "listado-tamanios": "SELECT current_database() AS database_name, schemaname AS schema_name, tablename AS table_name, pg_size_pretty(pg_total_relation_size(schemaname || '.' || tablename)) AS total_size, pg_size_pretty(pg_relation_size(schemaname || '.' || tablename)) AS table_size, pg_size_pretty(pg_indexes_size(schemaname || '.' || tablename)) AS index_size FROM pg_tables;"
    }
    

    #funcion para obtener la consulta me devuelve una lista de duplas con los resultados
    def obtener_consulta(consulta):
        with connection.cursor() as cursor:
            cursor.execute(consultas[consulta])
            resultado = cursor.fetchall()
            nombre_columnas = [desc[0] for desc in cursor.description]
        return resultado, nombre_columnas
    
    resultado, nombre_columnas = obtener_consulta(consulta) 
    lista_resultado = [list(tupla) for tupla in resultado]
    consultaHecha = consultas[consulta] #Esto para mostrar la consulta hecha en el template
    return render(request,'resultado.html',{'consulta':consultaHecha,'resultados':lista_resultado,'columnas':nombre_columnas})

    #USAR CUANDO ESTEN LOS GRAFICOS
    #resultado,nombre_columnas=obtener_consulta(consulta) 
    #lista_resultado=[list(tupla) for tupla in resultado]
    #hay_grafico='no' if grafico==0 else 'si' 
    #print(lista_resultado)
    #return render(request,'resultado.html',{'resultados':lista_resultado,'columnas':nombre_columnas,'grafico':grafico})



 