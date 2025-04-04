from fastapi import FastAPI
import qrcode
from fastapi.responses import StreamingResponse
from io import BytesIO

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/qrActivoFijo/{data}")
async def generate_qr(data: str):
    """
    Generate a QR code for the given data and return it as an image.
    """
    #
    data = "https://example.com/" + data

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        fill_color="black", 
        back_color="white"
    )

    # Save the image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)

    # Return the image as a StreamingResponse
    return StreamingResponse(img_io, media_type="image/png")
