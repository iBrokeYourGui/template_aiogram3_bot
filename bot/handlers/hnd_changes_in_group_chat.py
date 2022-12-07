"""
Здесь дан пример обработки событий внутри публичного чата
Чат задается через config.main_chat_id
"""

from aiogram import F, Router, Bot
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, KICKED, LEFT, RESTRICTED, MEMBER, ADMINISTRATOR, CREATOR
from aiogram.types import ChatMemberUpdated

from bot.config import config

changes_in_group_router = Router()
changes_in_group_router.chat_member.filter(F.chat.id == config.main_chat_id)


@changes_in_group_router.chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=
        (KICKED | LEFT | RESTRICTED | MEMBER)
        >>
        (ADMINISTRATOR | CREATOR)
    )
)
async def admin_promoted(event: ChatMemberUpdated, admins: set[int], bot: Bot):
    admins.add(event.new_chat_member.user.id)
    await bot.send_message(
        event.chat.id,
        f"{event.new_chat_member.user.first_name} "
        f"был(а) повышен(а) до Администратора!"
    )


@changes_in_group_router.chat_member(
    ChatMemberUpdatedFilter(
        # Обратите внимание на направление стрелок
        # Или можно было поменять местами объекты в скобках
        member_status_changed=
        (KICKED | LEFT | RESTRICTED | MEMBER)
        <<
        (ADMINISTRATOR | CREATOR)
    )
)
async def admin_demoted(event: ChatMemberUpdated, admins: set[int], bot: Bot):
    admins.discard(event.new_chat_member.user.id)
    await bot.send_message(
        event.chat.id,
        f"{event.new_chat_member.user.first_name} "
        f"был(а) понижен(а) до обычного юзера!"
    )