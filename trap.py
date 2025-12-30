import socket
import os

def start_security_trap():
    # المنفذ الوهمي اللي هيغري أي حد يحاول يفحص جهازك
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.bind(('0.0.0.0', port))
        s.listen(5)
        print(f"[*] المصيدة نشطة الآن على بورت {port}...")
        print("[*] في انتظار أي محاولة اختراق للرد عليها صوتياً...")
        
        while True:
            client, addr = s.accept()
            alert_msg = f"Alert! Unauthorized access attempt from IP {addr[0]}"
            print(f"\n[!!!] تنبيه: محاولة دخول من: {addr[0]}")
            
            # أمر جعل الموبايل ينطق التنبيه بصوت عالي
            os.system(f'termux-tts-speak "{alert_msg}"')
            
            # إغلاق الاتصال بعد تسجيل البيانات
            client.send(b"Access Denied! Your information has been logged.\n")
            client.close()
            
    except Exception as e:
        print(f"حدث خطأ: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    start_security_trap()

