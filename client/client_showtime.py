import grpc

import showtime_pb2
import showtime_pb2_grpc


def get_schedule_by_date(stub,date):
    """
        Request showtime service to get the schedule of a date
        Argument:
            - date : showtime_pb2.ScheduleDate, the date we want to get the schedule of
    """
    schedule = stub.GetScheduleByDate(date)
    print(schedule)

def get_list_schedule(stub):
    """
        Request showtime service to get all the schedules in db
    """
    allschedule = stub.GetSchedule(showtime_pb2.Empty())
    for schedule in allschedule:
        print("Date %s" % (schedule.date))

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:3002') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)

        print("-------------- GetScheduleByDate --------------")
        scheduleDate = showtime_pb2.ScheduleDate(date="20151130")
        get_schedule_by_date(stub, scheduleDate)
        
        print("-------------- GetListSchedule --------------")
        get_list_schedule(stub)

    channel.close()

if __name__ == '__main__':
    run()
