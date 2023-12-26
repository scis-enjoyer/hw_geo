from aiogram.fsm.state import StatesGroup, State


class Quiz(StatesGroup):
    first_answer = State() # промт пользователей
    second_answer = State()
    third_answer = State()
    foutrh_answer = State()
    fifth_answer = State()
    end = State()