import datetime

date = datetime.date


def get_table_1_data():
    return [{
        "goods_id": 123,
        "employee": "小王",
        "start_date": date(2016, 12, 16),
        "end_date": date(2018, 8, 15)
    }, {
        "goods_id": 123,
        "employee": "小李",
        "start_date": date(2018, 8, 16),
        "end_date": date(2019, 12, 30)
    }, {
        "goods_id": 123,
        "employee": "小张",
        "start_date": date(2019, 12, 31),
        "end_date": date(2020, 6, 30)
    }]


def get_table_2_data():
    return [{
        "goods_id": 123,
        "status": "orderd",
        "start_date": date(2016, 12, 16),
        "end_date": date(2018, 11, 11)
    }, {
        "goods_id": 123,
        "status": "prepared",
        "start_date": date(2018, 11, 12),
        "end_date": date(2019, 12, 22)
    }, {
        "goods_id": 123,
        "status": "delivery",
        "start_date": date(2019, 12, 23),
        "end_date": date(2020, 2, 11)
    }, {
        "goods_id": 123,
        "status": "finish",
        "start_date": date(2020, 2, 12),
        "end_date": date(2020, 6, 30)
    }]


def person_in_charge(person_record, status_start_date, status_end_date):
    start_data_in = status_start_date >= person_record['start_date'] and status_start_date <= person_record[
        'end_date'];
    end_data_in = status_end_date >= person_record['start_date'] and status_end_date <= person_record['end_date']
    return start_data_in or end_data_in


def output(record_line):
    # 在这里输出到你要输出的地方
    print(record_line)
    # pass


def handle_data():
    data_1 = get_table_1_data()  # person data
    data_2 = get_table_2_data()  # status data

    # Step 1. 拿到所有的 goods_id
    goods_id_set = set()  # 创建一个集合
    for item in data_2:
        goods_id_set.add(item['goods_id'])

    # Step 2. 开始处理
    for gid in goods_id_set:
        status_record_list = filter(lambda v: v['goods_id'] == gid, data_2)

        for status_record in status_record_list:

            # 下面这行被注释掉的的意思 和下面 连续两次的filter 意思一样
            # person_record_list = filter(lambda person_record: person_record['goods_id'] == gid and person_in_charge(person_record, status_record['start_date'], status_record['end_date']), data_1)

            # 处理这个状态记录

            # 第一步筛选出 商品id 符合的记录
            person_record_list = filter(lambda person_record: person_record['goods_id'] == gid, data_1)
            person_record_list = list(person_record_list)

            # 第二步 筛选出在当前状态日期范围内的人员记录
            person_record_list = filter(
                lambda p: person_in_charge(p, status_record['start_date'], status_record['end_date']),
                person_record_list)
            person_record_list = list(person_record_list)

            # print("currnet stat" + str(status_record) + " ---  " + str(person_record_list))

            # 针对每一个人员记录
            for pr in person_record_list:
                result = {
                    "goods_id": gid,
                    "status": status_record['status'],
                    "start_date": max(pr['start_date'], status_record['start_date']),
                    "end_date": min(pr['end_date'], status_record['end_date']),
                    "employee": pr['employee']
                }
                output(result)


if __name__ == '__main__':
    handle_data()
