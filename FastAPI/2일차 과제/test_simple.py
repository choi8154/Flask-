# from datetime import datetime, timedelta
#
# DELIVERY_DAYS = 2 # 상수를 사용하여 값의 배경을 알려줌
#
# def _is_holiday(day: datetime) -> bool:
#     return day.weekday() > 5
#
# def get_eta(purchase_date: datetime) -> datetime:
#     current_date = purchase_date
#     remaining_day = DELIVERY_DAYS
#
#     while remaining_day > 0:
#         current_date += timedelta(days=1)
#         if not _is_holiday(current_date):
#             remaining_day -= 1
#
#     return current_date
#
# def test_get_eat_2023_12_01()-> None:
#     result = get_eta(datetime(2023, 12, 1))
#     assert result == datetime(2023, 12, 4)
#
#
# def test_get_eta_2024_12_31() -> None:
#     """
#     공휴일 정보가 없어서 1월 1일도 평일로 취급됩니다.
#     """
#     result = get_eta(datetime(2024, 12, 31))
#     assert result == datetime(2025, 1, 2), "기간이 맞지 않습니다."
#
# def test_get_eta_2024_02_28() -> None:
#     result = get_eta(datetime(2024, 2, 28))
#     assert result == datetime(2024, 3, 1)
