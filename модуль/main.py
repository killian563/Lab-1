from Passenger import Passenger
from Route import Route
from Shedule import Shedule
from Station import Station
from Transport import Bus
import pymysql
from config import host, user, password, db_name

connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
)
print("successfully connected...")
print("#" * 20)

    # create table
# with connection.cursor() as cursor:
#     create_table_query = "CREATE TABLE `logistics`(id int AUTO_INCREMENT," \
#                          " person varchar(32)," \
#                          " title varchar(32)," \
#                          " station1 varchar(32)," \
#                          " station2 varchar(32)," \
#                          " departureTime varchar(32)," \
#                          " arrivalTime varchar(32), PRIMARY KEY (id));"
#     cursor.execute(create_table_query)
#     print("Table created successfully")

    # drop table
# with connection.cursor() as cursor:
#     drop_table_query = "DROP TABLE `logistics`;"
#     cursor.execute(drop_table_query)
#     print("Table droped successfully")

    # delete data
# with connection.cursor() as cursor:
#     delete_query = "DELETE FROM `logistics` WHERE id = 5;"
#     cursor.execute(delete_query)
#     connection.commit()

    # insert data


def commit_route(person, transport, station_a, station_b, time_departure, time_arrive):
    with connection.cursor() as cursor:
        insert_query = f"INSERT INTO `logistics` (person, title, station1, station2, departureTime, arrivalTime) \
            VALUES ('{person.surname}', '{transport.title}', '{station_a.title}', '{station_b.title}','{time_departure}','{time_arrive}');"
        cursor.execute(insert_query)
        connection.commit()

    print("#" * 20)


def show_shedule():
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `logistics`"
        cursor.execute(select_all_rows)
        # cursor.execute("SELECT * FROM `users`")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("#" * 20)


sch = Shedule('Schedule')
station_1 = Station(1, 'Kyiv', 51.4861639, 31.2691622)
station_2 = Station(2,'Frankivsk', 48.9253122, 24.7235424)
bus1 = Bus('ElectroBus', 30)
station_3 = Station(3, 'Lviv TrainStation', 49.8399319, 23.9937661)
bus2 = Bus('FastBus', 36)
person1 = Passenger('Tom')
person2 = Passenger('Robert')
route1 = Route(sch)
route2 = Route(sch)
route1.route_create(bus1, station_1, station_2)
route2.route_create(bus2, station_2, station_3)

person1.buy_ticket(station_1, station_2, bus1)
person2.buy_ticket(station_2, station_3, bus2)
# sch.print_schedule()

commit_route(person1, bus1, station_1, station_2, str(route1.route_info['routes'][0]['summary']['departureTime']), str(route1.route_info['routes'][0]['summary']['arrivalTime']))
commit_route(person2, bus2, station_3, station_3, str(route2.route_info['routes'][0]['summary']['departureTime']), str(route2.route_info['routes'][0]['summary']['arrivalTime']))

show_shedule()

connection.close()