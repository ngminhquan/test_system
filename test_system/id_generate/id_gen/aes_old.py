import math
#Input

#pt = '0123456789abcdeffedcba9876543210'
#key = '0f1571c947d9e8590cb7add6af7f6798'
#cp = 'ff0b844a0853bf7c6934ab4364148fb9'

#ASCII to hex
def text_to_hex(s):
    d = ''
    c = []
    for i in s:
        c.append(hex(ord(i)))
    for i in range(len(c)):
        c[i] = c[i].replace('0x', '')
    for i in range(len(c)):
        if len(c[i]) == 1:
            c[i] = '0' + c[i]
    for i in c:
        d += i
    d = d.upper()
    return d

#print(text_to_hex('a\nb'))
#hex to ASCII
def hex_to_text(s):
    hex_pt =[]
    text =''
    for i in range(0,len(s),2):
        hex_pt.append(bin_to_dec(int(hex_to_bin(s[i:i+2]))))
    for i in range(len(hex_pt)):
        text += chr(hex_pt[i])
    return text
  
#print(hex_to_text(text_to_hex('a\nb')))
#print(int('a', 16))
#add two hexa
def add_hex(a, b):
    c = int(a, 16) + int(b, 16)
    c = bin_to_hex(dec_to_bin(c))
    return c

#Transform hexadecimal to binary
def hex_to_bin(s):
    trans = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"}
    binary = ""
    for i in range(len(s)):
        binary = binary + trans[s[i]]
    return binary

#Transform binary to hexadecimal
def bin_to_hex(s):
    trans = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"}
    hexa = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch += s[i]
        ch += s[i+1]
        ch += s[i+2]
        ch += s[i+3]
        hexa = hexa + trans[ch]
    return hexa

#Transform decimal to binary
def dec_to_bin(s):
    res = bin(s).replace("0b", "") # loai bo 0b cua ham bin
    if(len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res

#Transform decimal to binary
def dec_to_bin8(s):
    res = bin(s).replace("0b", "") # loai bo 0b cua ham bin
    if(len(res) % 8 != 0):
        div = len(res) / 8
        div = int(div)
        counter = (8 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


#Transform binary to decimal
def bin_to_dec(s):
    dec, i = 0, 0
    while (s != 0):
        r = s % 10
        dec += r * pow(2,i)
        s //= 10
        i += 1
    return dec

#permutation
def permute(k, arr, n):
    permutation = ''
    for i in range(0, n):
        permutation += k[arr[i]-1]
    return permutation

#Chia thanh cac khoi n-byte (8*n-bit)
def divide(s, n):
    a = []
    for i in range(0, len(s), n):
        a.append(s[i:i + n])
    for i in range(len(a)):
        if len(a[i]) < n:
            a[i] += '8'
            for j in range(0, n):
                if len(a[i]) == n:
                    break
                a[i] += '0'
    return a

#phép cộng modulo 2^m
def add(a, b, m):
    val = int(a, 16) + int(b, 16)
    while val > int(math.pow(2, m)):
        val = val - int(math.pow(2, m))        #đưa về giá trị trong modulo 2^b
    val = hex(val).replace('0x', '') 
    s = ''
    while 1:
        if len(s) + len(val) == m/4:
            s += val
            break                               #padding các bit '0' để số đầu ra
        s += '0'                                #tương ứng là m_bit (m/4 số hexa)
    s = s.upper()
    return s

#S_box
Sbox = [['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
        ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
        ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
        ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
        ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
        ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
        ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
        ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
        ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
        ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
        ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
        ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
        ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
        ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
        ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
        ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']]

#Substitute Bytes Transformation
def subBytes(s):
    s = hex_to_bin(s)       #Chuyen ve nhi phan
    value = ''
    for i in range(0, 16):
        left4 = ''
        right4 = ''
        left4 += s[i * 8] + s[i * 8 + 1] + s[i * 8 +2] + s[i * 8 + 3]       #4 bit trai
        right4 += s[i * 8 + 4] + s[i * 8+ 5] + s[i * 8 +6] + s[i * 8 + 7]   #4 bit phai
        row = bin_to_dec(int(left4))        #xac dinh vi tri hang va cot
        col = bin_to_dec(int(right4))
        value += Sbox[row][col]             #tim gia tri dua tren Sbox
    return value
#print(subBytes(pt))

#ShiftRows Transformation
def shift(s, nth):      #ham dich vong trai n bits
    if nth == 0:
        return s
    else:
        for i in range(0, nth):             #dich trai 1 bits, thuc hien n lan
            k = ''
            for j in range(1, len(s)):      #lay tu bit[1] den het + bit[0]
                k += s[j]
            k += s[0]
            s = k
        return s

#print(shift('12345678', 2))
def matrixTrans(s):                         #chuyen chuoi ve ma tran
    k = 0
    b = []
    for i in range(0, 4):
        a = []
        for j in range(0, 4):
            a.append(s[k] + s[k + 1])       #moi phan tu cua ma tran gom 2 so hexa
            k += 2
        b.append(a)
    return b

#def matTrans(s, row, col):
#    k = 0
#    b = []
#    for i in range(0, row):
#        a = []
#        for j in range(0, col):
#            a.append(s[k] + s[k + 1])       #moi phan tu cua ma tran gom 2 so hexa
#            k += 2
#        b.append(a)
#    return b

def shiftRows(s):                           #
    value = ''
    a = matrixTrans(s)
    b = ''
    for i in range(0, 4):
        for j in range(0, 4):
            b += a[j][i]
    for i in range(0, 4):                   #cac phan tu o hang i dich vong trai i bits
        value += shift(b[i*8:i*8+8], 2 * i)
    return value

#MixColumns Transformation
multiMatrix = [['02', '03', '01', '01'],    #ma tran nhan trong mixColumns
               ['01', '02', '03', '01'],
               ['01', '01', '02', '03'],
               ['03', '01', '01', '02']]

def xor_hex(a, b):                          #xor 2 so hexa, output 1 so hexa
    a = hex_to_bin(a)
    b = hex_to_bin(b)
    c = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            c += '0'
        else: c += '1'
    c = bin_to_hex(c)
    return c

def xor(a, b):                              #xor 2 so nhi phan a, b
    c = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            c += '0'
        else: c += '1'
    return c

def multiplication(x, a):                   #phep nhan trong GF(2^8)
    x = hex_to_bin(x)
    a = hex_to_bin(a)
    y = x
    k = []
    for i in range(0, 8):
        if i == 0:
            k.append(y)
        else:
            if int(y[0]) == 0:
                for j in range(1, len(y)):
                    value += y[j]
                value += '0'
                y = value
                k.append(y)
            else:
                value = xor(y[1:] + '0', '00011011')
                y = value
                k.append(y)
        value = ''
    k.reverse()
    b = []
    for i in range(0, 8):
        if int(a[i]) == 1:
            b.append(k[i])
    val = b[0]
    for i in range(1, len(b)):
        if len(b) == 1:
            break
        else:
            val = xor(val, b[i])
    return bin_to_hex(val)


def mixColumns(s):                          #thuc hien mixColumns
    a = []
    b = ''
    s = matrixTrans(s)
    for i in range(0, 4):                   #nhan ma tran dau vao voi multiMatrix
        for j in range(0, 4):               #phep toan duoc thuc hien trong truong GF(2^8)
            a = []
            for g in range(0, 4):           
                a.append(multiplication(s[g][j], multiMatrix[i][g]))    #phep nhan trong GF(2^8)
            for j in range(0, 4):
                a[j] = hex_to_bin(a[j])
            value = xor(xor(a[0], a[1]), xor(a[2], a[3]))           #phep cong trong GF(2^8)
            value = bin_to_hex(value)
            b += value
    c = matrixTrans(b)
    d = ''
    for i in range(0, 4):
        for j in range(0, 4):
            d += c[j][i]
    return d

#AddRoundKey Transformation
def addKey(s, rk):                          #thuc hien xor input va roundkey(16bytes)
    s = hex_to_bin(s)
    rk = hex_to_bin(rk)
    value = xor(s, rk)
    return bin_to_hex(value)

#Key expansion
def rotword(s):                             #dich vong trai 1 byte
    value = ''
    for i in range(1, 4):
        value += (s[2 * i]+s[2 * i+1])
    value += (s[0] + s[1])
    return value


def subword(s):                             #thay the tung byte cua input thong qua Sbox
    s = hex_to_bin(s)
    value = ''
    for i in range(0, 4):
        left4 = ''
        right4 = ''
        left4 += s[i * 8] + s[i * 8 + 1] + s[i * 8 +2] + s[i * 8 + 3]       #4 bit trai
        right4 += s[i * 8 + 4] + s[i * 8+ 5] + s[i * 8 +6] + s[i * 8 + 7]   #4 bit phai
        row = bin_to_dec(int(left4))        #xac dinh vi tri hang va cot
        col = bin_to_dec(int(right4))
        value += Sbox[row][col]             #tim gia tri dua tren Sbox
    return value

#print(subword(rotword('7F8D292F')))


def keyExpansion(key):                      #mo rong key tu 16bytes thanh 176bytes
    w = []
    for i in range(0, 4):
        w.append(key[8 * i] + key[8 * i + 1]+
                 key[8 * i + 2] + key[8 * i + 3]+
                 key[8 * i + 4] + key[8 * i + 5]+
                 key[8 * i + 6] + key[8 * i + 7])
    Rcon = []                   #round constant, thuc hien XOR voi input[i] o vong thu i
    value = '01'
    for i in range(0, 10):
        Rcon.append(value)
        value = multiplication(value, '02')

    for i in range(4, 44):      #thuc hien mo rong key thanh 44 words
        temp = w[i-1]
        if i % 4 == 0:
            temp = subword(rotword(temp))
            temp = hex_to_bin(temp)
            rcon = Rcon[int(i/4) - 1] + '000000'
            rcon = hex_to_bin(rcon)
            temp = bin_to_hex(xor(temp, rcon))
        w.append(xor(hex_to_bin(temp), hex_to_bin(w[i - 4])))
        w[i] = bin_to_hex(w[i])
    return w

#print(keyExpansion(key))

def printMatrix(s):        
    k = 0
    b = []
    for i in range(0, 4):
        a = []
        for j in range(0, 4):
            a.append(s[k] + s[k + 1])       #moi phan tu cua ma tran gom 2 so hexa
            k += 2
        b.append(a)
    c = ''
    for i in range(0, 4):
        for j in range(0, 4):
            c += b[j][i]
    d = matrixTrans(c)
    for i in range(0, 4):
        print(d[i], end = '\n')

#printMatrix(pt)

#Encrypt 
def encrypt(pt, key):
    pt = pt.upper()
    key = key.upper()
    w = keyExpansion(key)
    k0 = w[0] + w[1] + w[2] + w[3]
    pt = addKey(pt, k0)
    for i in range(1, 10):
        aftersub = subBytes(pt)
        aftershift = shiftRows(aftersub)
        aftermix = mixColumns(aftershift)
        rk = w[i * 4] + w[i * 4 + 1] + w[i * 4 + 2] + w[i * 4 + 3]
        pt = addKey(aftermix, rk)
    last_sub = subBytes(pt)
    last_shift = shiftRows(last_sub)
    #mixColumns(pt)
    c = matrixTrans(last_shift)
    d = ''
    for i in range(0, 4):
        for j in range(0, 4):
            d += c[j][i]
    k10 = w[40] + w[41] + w[42] + w[43]
    cipher = addKey(d, k10)
    return cipher

#print(encrypt(pt, key))


