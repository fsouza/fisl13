import greenlet
import MySQLdb

N_THREADS = 2


class MySQLQuery(greenlet.greenlet):

    def run(self):
        conn = MySQLdb.connect(host="localhost", port=3306, user="root", db="fisl")
        try:
            conn.query("select sleep(2)")
            result = conn.use_result()
            result.fetch_row()
        finally:
            conn.close()

if __name__ == '__main__':
    for i in range(N_THREADS):
        MySQLQuery().switch()
