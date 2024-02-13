import qrcode
from io import BytesIO
import base64


def generate_qr_img(vcard_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert image to BytesIO object
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    qr_image = base64.b64encode(buffer.getvalue()).decode()
    return qr_image


def generate_url(request):
    # Constructing the complete URL dynamically
    username = request.session.get('vcard_data')['name'].replace(' ', '').lower()
    scheme = request.scheme
    host = request.get_host()
    vcard_url = f"{scheme}://{host}/vcard/{username}"
    return vcard_url
