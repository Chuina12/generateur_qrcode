import qrcode

def generate_qrcode(data, file_path):
    """
    Génère un QR code à partir des données fournies et le sauvegarde dans le fichier spécifié.
    
    :param data: Les données à encoder dans le QR code.
    :param file_path: Le chemin du fichier où sauvegarder le QR code généré.
    """
    # Crée une instance de QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Ajoute les données au QRCode
    qr.add_data(data)
    qr.make(fit=True)

    # Crée une image du QRCode
    img = qr.make_image(fill='black', back_color='white')

    # Sauvegarde l'image du QRCode
    img.save(file_path)
    print(f"QR code sauvegardé en tant que {file_path}")

if __name__ == "__main__":
    # Exemple d'utilisation du script
    data = "https://www.kapver-schop.de"
    file_path = "kapver-schop.png"
    generate_qrcode(data, file_path)
