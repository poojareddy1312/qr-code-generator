import qrcode
import image

data = "https://web.whatsapp.com/"


qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4,  # Thickness of the border (minimum is 4)
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)  # Adjusts the size to fit the data

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR Code generated and saved as 'qrcode.png'")

