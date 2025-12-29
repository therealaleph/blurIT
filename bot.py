import asyncio
import os
import tempfile
import subprocess
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


class BlurState(StatesGroup):
    waiting_for_percentage = State()


def blur_video(input_path: str, output_path: str, blur_percentage: int) -> None:
    sigma = (blur_percentage / 100.0) * 50.0
    
    cmd = [
        'ffmpeg', '-y', '-i', input_path,
        '-vf', f'gblur=sigma={sigma}',
        '-c:v', 'libx264',
        '-preset', 'fast',
        '-crf', '23',
        '-c:a', 'copy',
        '-movflags', '+faststart',
        output_path
    ]
    
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg error: {result.stdout}")


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Send me a video file and I will blur it for you.")


@dp.message(F.video | F.document)
async def handle_video(message: Message, state: FSMContext):
    file_id = None
    
    if message.video:
        file_id = message.video.file_id
        await state.update_data(file_id=file_id, file_type="video")
    elif message.document and message.document.mime_type and "video" in message.document.mime_type:
        file_id = message.document.file_id
        await state.update_data(file_id=file_id, file_type="document")
    
    if file_id:
        await state.set_state(BlurState.waiting_for_percentage)
        await message.answer("Please send the blur percentage (1-100):")


@dp.message(BlurState.waiting_for_percentage)
async def handle_percentage(message: Message, state: FSMContext):
    try:
        percentage = int(message.text.strip())
        if not 1 <= percentage <= 100:
            await message.answer("Please enter a number between 1 and 100.")
            return
    except ValueError:
        await message.answer("Please enter a valid number between 1 and 100.")
        return
    
    data = await state.get_data()
    file_id = data.get("file_id")
    
    if not file_id:
        await message.answer("No video file found. Please send a video first.")
        await state.clear()
        return
    
    processing_msg = await message.answer("Processing video...")
    
    try:
        file = await bot.get_file(file_id)
        
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = os.path.join(temp_dir, "input_video.mp4")
            output_path = os.path.join(temp_dir, "output_video.mp4")
            
            await bot.download_file(file.file_path, input_path)
            
            await asyncio.get_event_loop().run_in_executor(
                None, blur_video, input_path, output_path, percentage
            )
            
            if not os.path.exists(output_path):
                raise FileNotFoundError("Output video was not created")
            
            output_file = FSInputFile(output_path, filename="blurred_video.mp4")
            await message.answer_video(output_file)
            await processing_msg.delete()
    
    except Exception as e:
        await processing_msg.edit_text(f"Error processing video: {str(e)}")
    
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

