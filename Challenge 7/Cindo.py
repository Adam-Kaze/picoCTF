import sys

sys.stdout.reconfigure(encoding='utf-8')

# MAIN PROGRAM DECODE
text = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽'
flag = ''
for i in range(0, len(text)):
    flag += chr(ord(text[i]) >> 8)
    flag += chr(ord(text[i]) - ((ord(text[i]) >> 8) << 8))
print(f'Decode : {flag} + \n')

# DETAIL PROGRAM
print('Detail :')
for i in range(0, len(text)):
    a = ord(text[i]) >> 8
    print('a = ' + str(a) + ' = ', chr(a))
    b = ord(text[i])
    print('b = ' + str(b) + ' = ', chr(b))
    c = a << 8
    print('c = ' + str(c) + ' = ', chr(c))
    d = b - c
    print(str(b) + ' - ' + str(c) + ' = ' + str(d) + ' = ', chr(d) + '\n')

#   Dapat disimpulkan bahwa b bukan sama dengan c, karena proses penggeseran biner '>> 8' tidak sama dengan '>> 8 << 8'.
#   ord() digunakan untuk mengonversi karakter Unicode menjadi bilangan bulat.
#   Unicode adalah standar yang lebih luas daripada ASCII dan mencakup banyak karakter yang tidak ada dalam set ASCII standar.
#   chr() digunakan untuk mengonversi bilangan bulat (integer) menjadi karakter ASCII yang sesuai.

# MAIN PROGRAM ENCODE
flag = 'picoCTF{16_bits_inst34d_of_8_0ddcd97a}'
text = ''
for i in range(0, len(flag), 2):
    char1 = flag[i]
    char2 = flag[i + 1]
    ascii_value = (ord(char1) << 8) + ord(char2)
    text += chr(ascii_value)
print(f'Encode : {text}')
