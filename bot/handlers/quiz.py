from aiogram import types, F, Router 
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from kb import  get_keyboard, start_btm, fq_menu, sq_menu, fiq_menu, fou_menu, fifth_menu

from aiogram.types import ChatMemberLeft
from aiogram.fsm.context import FSMContext
from states import Quiz
from aiogram.filters import Command, StateFilter


router = Router()

answ_1 = ["san_fran","washington","new_york","spb"]
answ_2 = ["50","49","52","6"]
answ_3 = ["Ford","Nike","Boeing","Diesel"]
answ_4 = ["9.8","12.2","4.9","2.3"]
#answ_5 = ["336","124","1000","23.3"]

@router.message(Command("start"))
async def start(message: Message,state: FSMContext):
    await message.answer("Квиз бот для семинара по географии по теме США\nСделан 11 классом МБОУСОШ 90 ",reply_markup=get_keyboard(start_btm))
    await state.set_state(Quiz.first_answer)


@router.callback_query(F.data == "start_btm")
async def first_question(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("IT столица США",reply_markup=get_keyboard(fq_menu))
    await state.set_state(Quiz.second_answer)


@router.callback_query(Quiz.second_answer)
async def first_answer_reg(callback: CallbackQuery, state: FSMContext):
    answer_1 = callback.data
    await callback.message.answer("Сколько звезд на флаге США?",reply_markup=get_keyboard(sq_menu))
    await state.update_data(answ_1=answer_1)
    await state.set_state(Quiz.third_answer)


@router.callback_query(Quiz.third_answer)
async def second_answer(callback: CallbackQuery, state: FSMContext):
    answer_2 = callback.data
    await state.update_data(answ_2=answer_2)
    await callback.message.answer("Какая компания не была создана в США", reply_markup=get_keyboard(fiq_menu))
    await state.set_state(Quiz.foutrh_answer)


@router.callback_query(Quiz.foutrh_answer)
async def third_answer(callback: CallbackQuery, state: FSMContext):
    answer_3 = callback.data
    await state.update_data(answ_3=answer_3)
    await callback.message.answer("Площадь США равна ", reply_markup=get_keyboard(fou_menu))
    await state.set_state(Quiz.fifth_answer)

@router.callback_query(Quiz.fifth_answer)
async def fourth_answer(callback: CallbackQuery, state: FSMContext):
    answer_4 = callback.data
    await state.update_data(answ_4=answer_4)
    await callback.message.answer("Сколько людей живет в США?", reply_markup=get_keyboard(fifth_menu))
    await state.set_state(Quiz.end)

@router.callback_query(Quiz.end)
async def last_answer(callback: CallbackQuery, state: FSMContext):
    mark = 0
    answer_5 = callback.data
    calculate = await state.get_data()

    if calculate['answ_1']=='san_fran':
        mark+=1

    if calculate['answ_2']=='50':
        mark+=1
    
    if calculate['answ_3']=='Diesel:
        mark+=1
    
    if calculate['answ_4']=='9.8':
        mark+=1
    
    if answer_5 == '336':
        mark+=1
    
    if mark == 5 or mark == 0:
        await callback.message.answer(f'Вы набрали {mark} баллов!')
        await state.clear()
    elif mark == 1:
        await callback.message.answer(f'Вы набрали {mark} балл!')
        await state.clear()
    else:
        await callback.message.answer(f'Вы набрали {mark} балла!')
        await state.clear()




