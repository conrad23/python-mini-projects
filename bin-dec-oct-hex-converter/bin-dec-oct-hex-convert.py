__author__ = 'conrad'
from sys import argv


def dec_to_bin(decimal):
    binStr = ""
    decimal = int(decimal)
    while decimal > 0:
        remainder = decimal % 2
        binStr += str(remainder)
        decimal /= 2
    string = binStr[::-1]
    return string


def dec_to_hex(decimal):
    binStr = ""
    decimal = int(decimal)
    while decimal > 0:
        remainder = decimal % 16
        if remainder == 10:
            binStr += "A"
        if remainder == 11:
            binStr += "B"
        if remainder == 12:
            binStr += "C"
        if remainder == 13:
            binStr += "D"
        if remainder == 14:
            binStr += "E"
        if remainder == 15:
            binStr += "F"
        if remainder < 10:
            binStr += str(remainder)
        decimal = decimal / 16
    string = binStr[::-1]
    return string


def dec_to_oct(decimal):
    binStr = ""
    decimal = int(decimal)
    while decimal > 0:
        remainder = decimal % 8
        binStr += str(remainder)
        decimal /= 8
    string = binStr[::-1]
    return string


def bin_to_dec(binary):
    result = 0
    binary = str(binary)
    while len(binary) > 1:
        operation = int(binary[:1])
        binary = binary[1:]
        result += operation
        result *= 2
    if int(binary) == 1:
        result += 1
    return result


def bin_to_hex(binary):
    decimal = bin_to_dec(binary)
    hexadecimal = dec_to_hex(decimal)
    return hexadecimal


def bin_to_oct(binary):
    decimal = bin_to_dec(binary)
    octal = dec_to_oct(decimal)
    return octal


def hex_to_dec(hexadecimal):
    binary = hex_to_bin(hexadecimal)
    decimal = bin_to_dec(binary)
    return decimal


def hex_to_bin(hexadecimal):
    hexadecimal = str(hexadecimal)
    binary = ""
    for i in range(0, len(hexadecimal)):
        if hexadecimal[i] == '0':
            binary += "0000"
        if hexadecimal[i] == '1':
            binary += "0001"
        if hexadecimal[i] == '2':
            binary += "0010"
        if hexadecimal[i] == '3':
            binary += "0011"
        if hexadecimal[i] == '4':
            binary += "0100"
        if hexadecimal[i] == '5':
            binary += "0101"
        if hexadecimal[i] == '6':
            binary += "0110"
        if hexadecimal[i] == '7':
            binary += "0111"
        if hexadecimal[i] == '8':
            binary += "1000"
        if hexadecimal[i] == '9':
            binary += "1001"
        if hexadecimal[i] == 'A':
            binary += "1010"
        if hexadecimal[i] == 'B':
            binary += "1011"
        if hexadecimal[i] == 'C':
            binary += "1100"
        if hexadecimal[i] == 'D':
            binary += "1101"
        if hexadecimal[i] == 'E':
            binary += "1110"
        if hexadecimal[i] == 'F':
            binary += "1111"
    while binary[0] != '1':
        binary = binary[1:]
    return binary


def hex_to_oct(hexadecimal):
    binary = hex_to_bin(hexadecimal)
    octal = bin_to_oct(binary)
    return octal


def oct_to_dec(octal):
    result = 0
    octal = str(octal)
    while len(octal) > 1:
        operation = int(octal[:1])
        octal = octal[1:]
        result += operation
        result *= 8
    result += int(octal)
    return result


def oct_to_bin(octal):
    decimal = oct_to_dec(octal)
    binary = dec_to_bin(decimal)
    return binary


def oct_to_hex(octal):
    decimal = oct_to_dec(octal)
    hexadecimal = dec_to_hex(decimal)
    return hexadecimal


script, convertFrom, number = argv

number = str(number)

if convertFrom.lower() == "dec":
    print "      Binary(2):  %r" % dec_to_bin(number)
    print "       Octal(8):  %r" % dec_to_oct(number)
    print "    Decimal(10):  %r" % str(number)
    print "Hexadecimal(16):  %r" % dec_to_hex(number)

if convertFrom.lower() == "bin":
    print "      Binary(2):  %r" % number
    print "       Octal(8):  %r" % bin_to_oct(number)
    print "    Decimal(10):  %r" % str(bin_to_dec(number))
    print "Hexadecimal(16):  %r" % bin_to_hex(number)

if convertFrom.lower() == "hex":
    print "      Binary(2):  %r" % hex_to_bin(number)
    print "       Octal(8):  %r" % hex_to_oct(number)
    print "    Decimal(10):  %r" % str(hex_to_dec(number))
    print "Hexadecimal(16):  %r" % number

if convertFrom.lower() == "oct":
    print "      Binary(2):  %r" % oct_to_bin(number)
    print "       Octal(8):  %r" % number
    print "    Decimal(10):  %r" % str(oct_to_dec(number))
    print "Hexadecimal(16):  %r" % oct_to_hex(number)
