import time
import schedule
from etl.coingecko_etl import run_etl
from config import CRYPTOCURRENCIES_TO_FETCH

def scheduled_etl():
    print("Starting scheduled ETL process for cryptocurrency data...")
    run_etl(CRYPTOCURRENCIES_TO_FETCH)
    print("Scheduled ETL process completed.")

def run_continuous_update():
    print("Starting continuous update process...")
    schedule.every(2).day.do(scheduled_etl)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--continuous":
        run_continuous_update()
    else:
        print("Starting one-time ETL process for cryptocurrency data...")
        run_etl(CRYPTOCURRENCIES_TO_FETCH)
        print("One-time ETL process completed.")
