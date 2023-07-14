# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import base64
import binascii
import io

from PIL import Image, ImageOps
# We can preload Ico too because it is considered safe
from PIL import IcoImagePlugin

from random import randrange

from odoo.exceptions import UserError
from odoo.tools.translate import _


# Preload PIL with the minimal subset of image formats we need
Image.preinit()
Image._initialized = 2


def base64_to_image(base64_source):
    """Return a PIL image from the given `base64_source`.

    :param base64_source: the image base64 encoded
    :type base64_source: string or bytes

    :return: the PIL image
    :rtype: PIL.Image

    :raise: UserError if the base64 is incorrect or the image can't be identified by PIL
    """
    try:
        return Image.open(io.BytesIO(base64.b64decode(base64_source)))
    except (OSError, binascii.Error):
        raise UserError(_("This file could not be decoded as an image file. Please try with a different file."))
