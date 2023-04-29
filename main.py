import yt_dlp
from pync import Notifier


ydl_opts = {
    'listformats': True
}

video_url = input("İndirmek istediğiniz videonun URL'sini giriniz: ")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(f'{video_url}', download=False)

formats = info['formats']

print('Mevcut formatlar:')
for i, f in enumerate(formats):
    print(f'{i+1}. {f["ext"]} - {f["format_note"]} - {f["height"]}p')

selected_format = int(input('İndirilecek format numarasını seçin: '))
selected_format_id = formats[selected_format-1]['format_id']

ydl_opts = {
    'format': selected_format_id
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

notification_title = "Video İndirici"
notification_message = "Video indirme işlemi başarıyla tamamlandı."

Notifier.notify(notification_message, title=notification_title)

