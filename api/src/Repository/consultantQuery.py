def query_db(mycursor, query, args=(), one=False):
    mycursor.execute(query, args)
    r = [dict((mycursor.description[i][0], value) \
              for i, value in enumerate(row)) for row in mycursor.fetchall()]
    return (r[0] if r else None) if one else r