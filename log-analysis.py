import psycopg2

DBNAME = "news"

# What are the most popular three articles of all time?
query_1_title = ("What are the most popular three articles of all time?")
query_1 = (
    "select articles.title, count(*) as views "
    "from articles join log on "
    "log.path like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")

# Who are the most popular article authors of all time?
query_2_title = ("Who are the most popular article authors of all time?")
query_2 = (
    "select authors.name, count(*) as views from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by views desc")

# On which days did more than 1% of requests lead to errors
query_3_title = ("On which days did more than 1% of requests lead to errors?")
query_3 = (
    "select day, perc from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "perc from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by perc desc) as final_query "
    "where perc >= 1")


def connect():
    """Connect to the PostgreSQL database. Returns a database connection """
    try:
        db = psycopg2.connect("dbname={}".format(DBNAME))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to the database")


def get_query_results(query):
    """Connect to the PostgreSQL database.
    Return query results for given query """
    db, cursor = connect()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def print_query_results(query_results):
    for i in range(0, len(query_results), 1):
        print ('\t{} - {}\t - {} views'.
               format(i + 1, query_results[i][0], str(query_results[i][1])))


def print_error_results(query_results):
    for results in query_results:
        print ('\t{} - {}% error'.format(results[0], str(results[1])))


if __name__ == '__main__':
    print (query_1_title)
    print_query_results(get_query_results(query_1))
    print(query_2_title)
    print_query_results(get_query_results(query_2))
    print(query_3_title)
    print_error_results(get_query_results(query_3))
