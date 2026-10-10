import struct
import zlib


''' a png image generator that takes in the width, height and pixel bytearray
    the data list must contain \x00 for every row beginning'''

def gen_png(file_name: str, width: int, height: int, data: list[tuple]):
    # creates binary data chunks along with the crc32 checksum
    def make_chunk(chunk_type: bytes,chunk_data)-> bytes: 
        length = struct.pack(">I", len(chunk_data))
        crc_input = chunk_type + chunk_data
        crc_checksum = struct.pack(">I", zlib.crc32(crc_input) & 0xFFFFFFFF )
        return length + crc_input + crc_checksum
    
    signature = b'\x89PNG\r\n\x1a\n' 

    ihdr_payload = struct.pack(
        b'>IIBBBBB',
        width,
        height,
        8,
        6,
        0,
        0,
        0
    )
    ihdr_chunk = make_chunk(b'IHDR', ihdr_payload)

    compressed_data = zlib.compress(bytes(data))
    idat_chunk = make_chunk(b'IDAT', compressed_data)

    iend_chunk = make_chunk(b'IEND', b'')

    png_data = signature + ihdr_chunk + idat_chunk + iend_chunk
    with open(file_name, "wb") as file: 
        file.write(png_data)

'''NOTE: this is a small note for me about how a png data works

    PNG contains a binary signature that assures that this is a png(\x89PNG\r\n\x1a\n)
    then comes the image header(IHDR), which is a binary data chunk with data about the PNG
    next is image data (IDAT), which is a DEFLATE compressed byte stream of RGBA
    lastly, the image data end point(IEND), signifying the end of the data stream'''