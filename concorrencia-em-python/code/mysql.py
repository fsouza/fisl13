import MySQLdb
import threading

N_THREADS = 64


class MySQLQuery(threading.Thread):

    def run(self):
        conn = MySQLdb.connect(host="localhost", port=3306, user="root", db="fisl")
        try:
            conn.query("select sleep(2)")
            result = conn.use_result()
            result.fetch_row()
        finally:
            conn.close()

if __name__ == '__main__':
    threads = []
    for i in range(N_THREADS):
        t = MySQLQuery()
        t.start()
        threads.append(t)
    for i in range(N_THREADS):
        t.join()
