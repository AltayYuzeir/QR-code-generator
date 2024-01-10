import qrcode
from PIL import Image
import gradio as gr

def resize_for_condition_image(input_image: Image.Image, resolution: int):
    input_image = input_image.convert("RGB")
    W, H = input_image.size
    k = float(resolution) / min(H, W)
    H *= k
    W *= k
    H = int(round(H / 64.0)) * 64
    W = int(round(W / 64.0)) * 64
    img = input_image.resize((W, H), resample=Image.LANCZOS)
    return img


def build_string_vcard(name, surname, phone, email, company, position, city, country):
    result = "BEGIN:VCARD\nVERSION:3.0\n"

    if name is not None and name != "":
        result += f"FN: {name}"

    if surname is not None and surname != "":
        result += f" {surname}\n"
    else :
        result += f"\n"
    
    if phone is not None and phone != "":
        result += f"TEL;CELL: {phone}\n"

    if email is not None and email != "":
        result += f"EMAIL;WORK;INTERNET: {email}\n"
        
    if company is not None and company != "":
        result += f"ORG: {company}\n"

    if position is not None and position != "":
        result += f"TITLE: {position}\n"
    
    if city is not None and city != "":
        result += f"ADR:;; {city}"

    if country is not None and country != "":
        result += f" {country}\n"    
    else:
        result += f"\n"
        
    result += f"END:VCARD"
    return result

def url_qr_code(text,size):
    qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
    qr.add_data(text)
    qr.make(fit=True)

    qrcode_image = qr.make_image(fill_color="black", back_color="white")
    qrcode_image = resize_for_condition_image(qrcode_image, size)
    return qrcode_image

def message_qr_code(text,size):
    qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
    qr.add_data(text)
    qr.make(fit=True)

    qrcode_image = qr.make_image(fill_color="black", back_color="white")
    qrcode_image = resize_for_condition_image(qrcode_image, size)
    return qrcode_image

def sms_qr_code(number,message, size):
    qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
    
    text = f"SMSTO:{number}:message"
    
    qr.add_data(text)
    qr.make(fit=True)

    qrcode_image = qr.make_image(fill_color="black", back_color="white")
    qrcode_image = resize_for_condition_image(qrcode_image, size)
    return qrcode_image

def wifi_qr_code(name,password, size):
    qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
    
    text = f"WIFI:S:{name};T:WPA;P:{password};;"
    
    qr.add_data(text)
    qr.make(fit=True)

    qrcode_image = qr.make_image(fill_color="black", back_color="white")
    qrcode_image = resize_for_condition_image(qrcode_image, size)
    return qrcode_image

def email_qr_code(email,subject,message, size):
    qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
    
    text = f"MATMSG:TO:{email};SUB:{subject};BODY:{message};;"
    
    qr.add_data(text)
    qr.make(fit=True)

    qrcode_image = qr.make_image(fill_color="black", back_color="white")
    qrcode_image = resize_for_condition_image(qrcode_image, size)
    return qrcode_image

def vcard_qr_code(name, surname, phone, email, company, position, city, country, size):
    qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
    
    text = build_string_vcard(name, surname, phone, email, company, position, city, country)
    
    qr.add_data(text)
    qr.make(fit=True)

    qrcode_image = qr.make_image(fill_color="black", back_color="white")
    qrcode_image = resize_for_condition_image(qrcode_image, size)
    return qrcode_image

with gr.Blocks(title="QR code generator", css="footer {visibility: hidden}") as app:   
    
    with gr.Row():
        with gr.Tab("🌐 URL"):
            url_text = gr.Textbox(label="Website (URL)", value="https://www.instagram.com/cleverqrcodes")
            url_size = gr.Slider(label = "Height and Width", minimum=768, maximum=2048, value=768, step=1)
            url_button = gr.Button("▶️ Run")
        
        with gr.Tab("💬 Message"):
            message_text = gr.TextArea(label="Text")
            message_size = gr.Slider(label = "Height and Width", minimum=768, maximum=2048, value=768, step=1)
            message_button = gr.Button("▶️ Run")
            
        with gr.Tab("📱 SMS"):
            sms_number = gr.Textbox(label="Number")
            sms_message = gr.TextArea(label="Text")
            sms_size = gr.Slider(label = "Height and Width", minimum=768, maximum=2048, value=768, step=1)
            sms_button = gr.Button("▶️ Run")
            
        with gr.Tab("📻 Wi-Fi"):
            wifi_name = gr.Textbox(label="Wi-Fi name (SSID)")
            wifi_password = gr.Textbox(label="Password")
            wifi_size = gr.Slider(label = "Height and Width", minimum=768, maximum=2048, value=768, step=1)
            wifi_button = gr.Button("▶️ Run")
            
        with gr.Tab("📩 Email"):
            email_address = gr.Textbox(label="Email")
            email_subject = gr.Textbox(label="Subject")
            email_message = gr.TextArea(label="Message")
            email_size = gr.Slider(label = "Height and Width", minimum=768, maximum=2048, value=768, step=1)
            email_button = gr.Button("▶️ Run")
        
        with gr.Tab("🪪 VCard"):
            with gr.Row():
                vcard_name = gr.Textbox(label="Name")
                vcard_surname = gr.Textbox(label="Surname")
            
            with gr.Row():
                vcard_phone = gr.Textbox(label="Phone number")
                vcard_email = gr.Textbox(label="Email")
            
            with gr.Row():
                vcard_company = gr.Textbox(label="Company")
                vcard_position = gr.Textbox(label="Job position")
            
            with gr.Row():
                vcard_city = gr.Textbox(label="City")
                vcard_country = gr.Textbox(label="Country")
            
            vcard_size = gr.Slider(label = "Height and Width", minimum=768, maximum=2048, value=768, step=1)
            vcard_button = gr.Button("▶️ Run")
            
        output_image = gr.Image(label = "Resulting QR code image")
        
        url_button.click(fn = url_qr_code, inputs=[url_text,url_size], outputs=[output_image])
        
        message_button.click(fn = message_qr_code, 
                             inputs=[message_text,message_size],
                             outputs=[output_image])
        
        sms_button.click(fn = sms_qr_code, 
                           inputs=[sms_number,sms_message, sms_size],
                           outputs=[output_image])
        
        wifi_button.click(fn = wifi_qr_code, 
                           inputs=[wifi_name,wifi_password, wifi_size],
                           outputs=[output_image])
        
        email_button.click(fn = email_qr_code, 
                           inputs=[email_address,email_subject, email_message, email_size],
                           outputs=[output_image])
        
        vcard_button.click(fn=vcard_qr_code,
                           inputs=[vcard_name, vcard_surname, vcard_phone, vcard_email,
                                   vcard_company, vcard_position, vcard_city, vcard_country, vcard_size],
                           outputs=[output_image])
    
app.launch()
    
    
