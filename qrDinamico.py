import qrcode

import qrcode.constants
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer, GappedSquareModuleDrawer, HorizontalBarsDrawer, VerticalBarsDrawer, RoundedModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from PIL import ImageColor

module_drawers = {
    'circle': CircleModuleDrawer(),
    'square': GappedSquareModuleDrawer(),
    'horizontal': HorizontalBarsDrawer(),
    'vertical': VerticalBarsDrawer(),
    'rounded': RoundedModuleDrawer(),
    'default': SquareModuleDrawer()
}

error_correction = {
    'low': qrcode.constants.ERROR_CORRECT_L,
    'medium': qrcode.constants.ERROR_CORRECT_M,
    'quartile': qrcode.constants.ERROR_CORRECT_Q,
    'high': qrcode.constants.ERROR_CORRECT_H,
    'default': qrcode.constants.ERROR_CORRECT_M
}

def makeQR(data: str, logoURL: str, back_color: str = "#FFFFFF", edge_color: str = "#000000", center_color: str = "#000000", selected_drawer: str = "default", ratio: float = 0.5,box_size:int = 10, border:int = 4, selected_error: str = "default"):
    """
    Generates a QR code with a logo in the center and a radial gradient color mask.	
    """
    backColor = ImageColor.getcolor(back_color or "#FFFFFF", "RGB")
    edgeColor = ImageColor.getcolor(edge_color or "#000000", "RGB")
    centerColor = ImageColor.getcolor(center_color or "#000000", "RGB")

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=3,
        error_correction=error_correction.get(selected_error, error_correction['default']),
        box_size=box_size,
        border=border,
    )

    # Add data to the QR code
    qr.add_data(data)

    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=module_drawers.get(
            selected_drawer, module_drawers['default']),
        color_mask=RadialGradiantColorMask(
            back_color=backColor,
            edge_color=edgeColor,
            center_color=centerColor
        ),
        embeded_image_path=logoURL,
        embeded_image_ratio=ratio,

    )
    return img


if __name__ == "__main__":
    makeQR()
