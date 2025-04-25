from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from io import BytesIO
import qrDinamico


class QR(BaseModel):
    """
    Model for QR code data.
    """
    data: str
    logoURL: str
    back_color: str
    edge_color: str
    center_color: str
    selected_drawer: str
    selected_error: str
    ratio: float
    box_size: int
    border: int


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/qrActivoFijo")
async def generate_qr(qr: QR):
    """
    Generate a QR code for the given data and return it as an image.
    """
    # Create an image from the QR code instance
    img = qrDinamico.makeQR(
        qr.data,
        qr.logoURL,
        qr.back_color,
        qr.edge_color,
        qr.center_color,
        qr.selected_drawer,
        qr.ratio,
        qr.box_size,
        qr.border,
        qr.selected_error
    )

    # Save the image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)

    # Return the image as a StreamingResponse
    return StreamingResponse(img_io, media_type="image/png")
