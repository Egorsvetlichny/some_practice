import pdfplumber
from gtts import gTTS
from pathlib import Path


def convert_pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'Исходный файл: {Path(file_path).name}')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf_file:
            pages = [page.extract_text() for page in pdf_file.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        audio_pdf = gTTS(text=text, lang=language)
        file_name = f'{Path(file_path).stem}.mp3'
        audio_pdf.save(file_name)

        return f'Конвертация из pdf в mp3 прошла успешно! Файл {file_name} был сохранён!'
    else:
        return 'Исходного файла не существует!'


def main():
    file = input('Введите полный путь к pdf-файлу: ')
    lg = input('Укажите язык, например, "en" или "ru": ').lower()
    print(convert_pdf_to_mp3(file, lg))


if __name__ == '__main__':
    main()
