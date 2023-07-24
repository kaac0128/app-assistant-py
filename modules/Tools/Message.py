import pywhatkit as kit

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+57{number}", message)