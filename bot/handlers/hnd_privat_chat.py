from aiogram import F, Router
from aiogram.filters import ChatMemberUpdatedFilter, MEMBER, KICKED, Command
from aiogram.types import ChatMemberUpdated, Message

privat_chat_router = Router()
privat_chat_router.my_chat_member.filter(F.chat.type == 'private')
privat_chat_router.message.filter(F.chat.type == 'private')

# Здесь должна быть база данных
users = {111, 222}


@privat_chat_router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def user_blocked_bot(event: ChatMemberUpdated):
    print("Меня заблочили!")
    users.discard(event.from_user.id)


@privat_chat_router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def user_unblocked_bot(event: ChatMemberUpdated):
    print("Господин назначил меня любимой женой")
    users.add(event.from_user.id)


@privat_chat_router.message(Command(commands='users'))
async def show_users(message: Message):
    await message.answer("\n".join(f". {user_id}" for user_id in users))
