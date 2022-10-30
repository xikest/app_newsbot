
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from bots.bot_alert.src_generator.src_macro import SrcMacro
from tools.telegram_bot.contents import Context

# ================================================================================
# = 이벤트 작성
# ================================================================================

class EventHandler:
        # message reply function
        @staticmethod
        def get_message(update, context) :
            cont:Context
            user_text = update.message.text #
            if user_text == "안녕": 
                update.message.reply_text(text="안녕 하세요") 
            elif user_text == "일정": 
                update.message.reply_text(text="준비 중입니다.")
            # elif user_text == "shir": 
            #     update.message.reply_photo(photo=SrcMacro.ShillerRatio.compareWithPrice().content.pop())
            # elif user_text == "mkptn": 
            #     update.message.reply_photo(photo=SrcMacro.Market.pattern().content.pop()) 
  
            else:
                update.message.reply_text('아직은 학습 중입니다.')

        # help reply function
        @staticmethod
        def help_command(update, context) :
            update.message.reply_text("무엇을 도와드릴까요?")
          
           
        # shri reply function
        @staticmethod
        def shri_command(update, context) :
                update.message.reply_text("잠시만 기다려주세요.")
                for content in SrcMacro.ShillerRatio.compareWithPrice():
                    while len(content.content) > 0: update.message.reply_photo(photo=content.content.pop()) 
        
        # mkptn reply function
        @staticmethod
        def mkptn_command(update, context) :
                update.message.reply_text("잠시만 기다려주세요.")
                for content in SrcMacro.Market.pattern(): 
                    while len(content.content) > 0: update.message.reply_photo(photo=content.content.pop()) 
            
        # cpi reply function
        @staticmethod
        def cpi_command(update, context) :
                update.message.reply_text("잠시만 기다려주세요.")
                for content in SrcMacro.Macro.cpi(): 
                    while len(content.content) > 0: update.message.reply_photo(photo=content.content.pop()) 
            
        # reatailSales  reply function
        @staticmethod
        def reatailSales_command(update, context) :
                update.message.reply_text("잠시만 기다려주세요.")
                for content in SrcMacro.Macro.reatailSales(): 
                    while len(content.content) > 0: update.message.reply_photo(photo=content.content.pop()) 
                    
                    
                    
        @staticmethod
        def get_photo(update, context): 
            photo = context.bot.get_file(
                        update.message.photo[-1].file_id)
            photo.download()

        # file reply function
        @staticmethod
        def get_file(update, context) :
            file_id_short = update.message.document.file_id
            file_url =update.message.document.file_name
            context.bot.getFile(file_id_short).download(file_url)
            update.message.reply_text('file saved')
            
        @staticmethod
        def btns_task(update, context):  #task 버튼을 추가하는 함수입니다.
            task_buttons = [
                [
                    InlineKeyboardButton("Shiller Ratio", callback_data=1 ), InlineKeyboardButton("market pattern", callback_data=2 )
                    ], 
                [
                    InlineKeyboardButton("작업3", callback_data=3 ), InlineKeyboardButton("작업4", callback_data=4 )
                    ], 
                [
                    InlineKeyboardButton("종료", callback_data=9 )
                    ]
                ]
            reply_markup = InlineKeyboardMarkup( task_buttons )
            context.bot.send_message(
                chat_id=update.message.chat_id,
                text="작업을 선택해주세요.",
                reply_markup=reply_markup
                )
            
        @staticmethod
        def btns_action(update, context): #버튼을 클릭했을 때 실행되는 함수
            query = update.callback_query
            data = query.data
            
            context.bot.send_chat_action(
                chat_id=update.effective_user.id,
                action=ChatAction.TYPING
                )
            if data == "9":
                    context.bot.edit_message_text(text=f"작업이 종료되었습니다.",chat_id=query.message.chat_id, message_id=query.message.message_id)
                # elfif data == "2": context.bot.send_photo(text=f"작업이 종료되었습니다.",chat_id=query.message.chat_id, message_id=query.message.message_id)
            elif  data == "1": 
                    context.bot.send_photo(photo=SrcMacro.ShillerRatio.compareWithPrice().content.pop(), chat_id=query.message.chat_id)
                    
                    # context.bot.send_photo(photo=SrcMacro.ShillerRatio.compareWithPrice().content.pop(), chat_id=query.message.chat_id)
            elif data == "2": context.bot.send_photo(photo=SrcMacro.Market.pattern().content.pop(), chat_id=query.message.chat_id)
            else:
                context.bot.edit_message_text(
                    text=f"[{data}] 작업을 완료하였습니다.",
                    chat_id=query.message.chat_id,
                    message_id=query.message.message_id
                )
