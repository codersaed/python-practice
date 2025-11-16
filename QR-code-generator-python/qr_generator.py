import qrcode

def generate_qr(data, file_name):
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f"QR code saved as {file_name}")

def main():
    print("=== Simple QR Code Generator ===")
    data = input("Enter the URL or text to encode: ")
    file_name = input("Enter the file name to save (e.g., myqr.png): ")
    
    generate_qr(data, file_name)

if __name__ == "__main__":
    main()
