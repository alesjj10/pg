import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'

def read_header(file_name, header_length):
    """
    Načte binární soubor a vrátí prvních x (header_length) bajtů.
    """
    with open(file_name, 'rb') as soubor:
        return soubor.read(header_length)


def is_jpeg(file_name):
    """
    Vrátí True, pokud je soubor typu JPEG.
    """
    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header


def is_gif(file_name):
    """
    Vrátí True, pokud je soubor typu GIF.
    """
    header = read_header(file_name, len(gif_header1))
    return header == gif_header1 or header == gif_header2


def is_png(file_name):
    """
    Vrátí True, pokud je soubor typu PNG.
    """
    header = read_header(file_name, len(png_header))
    return header == png_header


def print_file_type(file_name):
    """
    Funkce vypíše typ souboru.
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')



    # přidej try-except blok, odchyť obecnou vyjímku Exception a vypiš ji
if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except FileNotFoundError:
        print('Chyba: Soubor nebyl nalezen.')
    except IndexError:
        print('Chyba: Zadejte cestu k souboru jako argument.')
    except Exception as e:
        print(f'Nastala neočekávaná chyba: {e}')