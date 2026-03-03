import pytchat
import time
import sys

# معرف الفيديو المباشر
video_id = "6_9ZiuONXt0"

def start_sync():
    print(f"[*] Starting Pytchat Engine for: {video_id}")
    try:
        chat = pytchat.create(video_id=video_id)
        
        while chat.is_alive():
            for c in chat.get().items:
                # طباعة مباشرة للمواصفات المطلوبة
                output = f"[{c.datetime}] {c.author.name}: {c.message}"
                try:
                    print(output)
                except UnicodeEncodeError:
                    # تعامل مع الرموز التعبيرية في الـ Terminal
                    print(output.encode('ascii', 'ignore').decode('ascii'))
                
                # ملاحظة: بما أنه لا يوجد سوبابيس، البيانات تظهر هنا فقط في الـ Logs
            time.sleep(1)
            
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    start_sync()
