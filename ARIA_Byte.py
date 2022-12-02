from __future__ import print_function

def S1box(pos):
    return [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
            [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
            [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
            [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
            [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
            [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
            [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
            [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
            [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
            [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
            [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
            [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
            [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
            [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
            [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
            [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]][pos//16][pos%16]

def S2box(pos):
    return [[0xe2, 0x4e, 0x54, 0xfc, 0x94, 0xc2, 0x4a, 0xcc, 0x62, 0x0d, 0x6a, 0x46, 0x3c, 0x4d, 0x8b, 0xd1],
            [0x5e, 0xfa, 0x64, 0xcb, 0xb4, 0x97, 0xbe, 0x2b, 0xbc, 0x77, 0x2e, 0x03, 0xd3, 0x19, 0x59, 0xc1],
            [0x1d, 0x06, 0x41, 0x6b, 0x55, 0xf0, 0x99, 0x69, 0xea, 0x9c, 0x18, 0xae, 0x63, 0xdf, 0xe7, 0xbb],
            [0x00, 0x73, 0x66, 0xfb, 0x96, 0x4c, 0x85, 0xe4, 0x3a, 0x09, 0x45, 0xaa, 0x0f, 0xee, 0x10, 0xeb],
            [0x2d, 0x7f, 0xf4, 0x29, 0xac, 0xcf, 0xad, 0x91, 0x8d, 0x78, 0xc8, 0x95, 0xf9, 0x2f, 0xce, 0xcd],
            [0x08, 0x7a, 0x88, 0x38, 0x5c, 0x83, 0x2a, 0x28, 0x47, 0xdb, 0xb8, 0xc7, 0x93, 0xa4, 0x12, 0x53],
            [0xff, 0x87, 0x0e, 0x31, 0x36, 0x21, 0x58, 0x48, 0x01, 0x8e, 0x37, 0x74, 0x32, 0xca, 0xe9, 0xb1],
            [0xb7, 0xab, 0x0c, 0xd7, 0xc4, 0x56, 0x42, 0x26, 0x07, 0x98, 0x60, 0xd9, 0xb6, 0xb9, 0x11, 0x40],
            [0xec, 0x20, 0x8c, 0xbd, 0xa0, 0xc9, 0x84, 0x04, 0x49, 0x23, 0xf1, 0x4f, 0x50, 0x1f, 0x13, 0xdc],
            [0xd8, 0xc0, 0x9e, 0x57, 0xe3, 0xc3, 0x7b, 0x65, 0x3b, 0x02, 0x8f, 0x3e, 0xe8, 0x25, 0x92, 0xe5],
            [0x15, 0xdd, 0xfd, 0x17, 0xa9, 0xbf, 0xd4, 0x9a, 0x7e, 0xc5, 0x39, 0x67, 0xfe, 0x76, 0x9d, 0x43],
            [0xa7, 0xe1, 0xd0, 0xf5, 0x68, 0xf2, 0x1b, 0x34, 0x70, 0x05, 0xa3, 0x8a, 0xd5, 0x79, 0x86, 0xa8],
            [0x30, 0xc6, 0x51, 0x4b, 0x1e, 0xa6, 0x27, 0xf6, 0x35, 0xd2, 0x6e, 0x24, 0x16, 0x82, 0x5f, 0xda],
            [0xe6, 0x75, 0xa2, 0xef, 0x2c, 0xb2, 0x1c, 0x9f, 0x5d, 0x6f, 0x80, 0x0a, 0x72, 0x44, 0x9b, 0x6c],
            [0x90, 0x0b, 0x5b, 0x33, 0x7d, 0x5a, 0x52, 0xf3, 0x61, 0xa1, 0xf7, 0xb0, 0xd6, 0x3f, 0x7c, 0x6d],
            [0xed, 0x14, 0xe0, 0xa5, 0x3d, 0x22, 0xb3, 0xf8, 0x89, 0xde, 0x71, 0x1a, 0xaf, 0xba, 0xb5, 0x81]][pos//16][pos%16]

def inv_S1box(pos):
    return [[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
            [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
            [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
            [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
            [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
            [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
            [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
            [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
            [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
            [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
            [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
            [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
            [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
            [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
            [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
            [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]][pos//16][pos%16]

def inv_S2box(pos):
    return [[0x30, 0x68, 0x99, 0x1b, 0x87, 0xb9, 0x21, 0x78, 0x50, 0x39, 0xdb, 0xe1, 0x72, 0x09, 0x62, 0x3c],
            [0x3e, 0x7e, 0x5e, 0x8e, 0xf1, 0xa0, 0xcc, 0xa3, 0x2a, 0x1d, 0xfb, 0xb6, 0xd6, 0x20, 0xc4, 0x8d],
            [0x81, 0x65, 0xf5, 0x89, 0xcb, 0x9d, 0x77, 0xc6, 0x57, 0x43, 0x56, 0x17, 0xd4, 0x40, 0x1a, 0x4d],
            [0xc0, 0x63, 0x6c, 0xe3, 0xb7, 0xc8, 0x64, 0x6a, 0x53, 0xaa, 0x38, 0x98, 0x0c, 0xf4, 0x9b, 0xed],
            [0x7f, 0x22, 0x76, 0xaf, 0xdd, 0x3a, 0x0b, 0x58, 0x67, 0x88, 0x06, 0xc3, 0x35, 0x0d, 0x01, 0x8b],
            [0x8c, 0xc2, 0xe6, 0x5f, 0x02, 0x24, 0x75, 0x93, 0x66, 0x1e, 0xe5, 0xe2, 0x54, 0xd8, 0x10, 0xce],
            [0x7a, 0xe8, 0x08, 0x2c, 0x12, 0x97, 0x32, 0xab, 0xb4, 0x27, 0x0a, 0x23, 0xdf, 0xef, 0xca, 0xd9],
            [0xb8, 0xfa, 0xdc, 0x31, 0x6b, 0xd1, 0xad, 0x19, 0x49, 0xbd, 0x51, 0x96, 0xee, 0xe4, 0xa8, 0x41],
            [0xda, 0xff, 0xcd, 0x55, 0x86, 0x36, 0xbe, 0x61, 0x52, 0xf8, 0xbb, 0x0e, 0x82, 0x48, 0x69, 0x9a],
            [0xe0, 0x47, 0x9e, 0x5c, 0x04, 0x4b, 0x34, 0x15, 0x79, 0x26, 0xa7, 0xde, 0x29, 0xae, 0x92, 0xd7],
            [0x84, 0xe9, 0xd2, 0xba, 0x5d, 0xf3, 0xc5, 0xb0, 0xbf, 0xa4, 0x3b, 0x71, 0x44, 0x46, 0x2b, 0xfc],
            [0xeb, 0x6f, 0xd5, 0xf6, 0x14, 0xfe, 0x7c, 0x70, 0x5a, 0x7d, 0xfd, 0x2f, 0x18, 0x83, 0x16, 0xa5],
            [0x91, 0x1f, 0x05, 0x95, 0x74, 0xa9, 0xc1, 0x5b, 0x4a, 0x85, 0x6d, 0x13, 0x07, 0x4f, 0x4e, 0x45],
            [0xb2, 0x0f, 0xc9, 0x1c, 0xa6, 0xbc, 0xec, 0x73, 0x90, 0x7b, 0xcf, 0x59, 0x8f, 0xa1, 0xf9, 0x2d],
            [0xf2, 0xb1, 0x00, 0x94, 0x37, 0x9f, 0xd0, 0x2e, 0x9c, 0x6e, 0x28, 0x3f, 0x80, 0xf0, 0x3d, 0xd3],
            [0x25, 0x8a, 0xb5, 0xe7, 0x42, 0xb3, 0xc7, 0xea, 0xf7, 0x4c, 0x11, 0x33, 0x03, 0xa2, 0xac, 0x60]][pos//16][pos%16]

def RotXOR(s, n, target):
    """
    Input: Byte array 's' of size 16, integer 'n', Byte array 'target' of size 16
    Output: Byte array of size 16 which is result of operation
    Right-rotate 's' by 'n' bits and XOR with 'target' then return the result
    """
    q = n//8
    n %= 8
    for i in range(16):
        target[(q+i) % 16] ^= (s[i] >> n)
        if (n != 0):
            target[(q+i+1) % 16] ^= ((s[i] << (8-n)) % 256)
    return target

def DiffLayer(i):
    """
    Input: Byte array 'i' of size 16
    Output: Byte array of size 16 which is diffusion of 'i'
    Diffuse 'i' and return it
    """
    o = [0] * 16
    T = i[ 3] ^ i[ 4] ^ i[ 9] ^ i[14]
    o[ 0] = i[ 6] ^ i[ 8] ^ i[13] ^ T
    o[ 5] = i[ 1] ^ i[10] ^ i[15] ^ T
    o[11] = i[ 2] ^ i[ 7] ^ i[12] ^ T
    o[14] = i[ 0] ^ i[ 5] ^ i[11] ^ T
    T = i[ 2] ^ i[ 5] ^ i[ 8] ^ i[15]
    o[ 1] = i[ 7] ^ i[ 9] ^ i[12] ^ T
    o[ 4] = i[ 0] ^ i[11] ^ i[14] ^ T
    o[10] = i[ 3] ^ i[ 6] ^ i[13] ^ T
    o[15] = i[ 1] ^ i[ 4] ^ i[10] ^ T
    T = i[ 1] ^ i[ 6] ^ i[11] ^ i[12]
    o[ 2] = i[ 4] ^ i[10] ^ i[15] ^ T
    o[ 7] = i[ 3] ^ i[ 8] ^ i[13] ^ T
    o[ 9] = i[ 0] ^ i[ 5] ^ i[14] ^ T
    o[12] = i[ 2] ^ i[ 7] ^ i[ 9] ^ T
    T = i[ 0] ^ i[ 7] ^ i[10] ^ i[13]
    o[ 3] = i[ 5] ^ i[11] ^ i[14] ^ T
    o[ 6] = i[ 2] ^ i[ 9] ^ i[12] ^ T
    o[ 8] = i[ 1] ^ i[ 4] ^ i[15] ^ T
    o[13] = i[ 3] ^ i[ 6] ^ i[ 8] ^ T
    return o

def KeyExpansion(key):
    """
    Input: Byte array 'key' of size 16/24/32
    Output: 13/15/17 size array of byte arrays each of size 16
    Generate encryption round keys
    """
    C = [[0x51, 0x7c, 0xc1, 0xb7, 0x27, 0x22, 0x0a, 0x94, 0xfe, 0x13, 0xab, 0xe8, 0xfa, 0x9a, 0x6e, 0xe0],
         [0x6d, 0xb1, 0x4a, 0xcc, 0x9e, 0x21, 0xc8, 0x20, 0xff, 0x28, 0xb1, 0xd5, 0xef, 0x5d, 0xe2, 0xb0],
         [0xdb, 0x92, 0x37, 0x1d, 0x21, 0x26, 0xe9, 0x70, 0x03, 0x24, 0x97, 0x75, 0x04, 0xe8, 0xc9, 0x0e]]
    R = len(key)//4 + 8
    idx = len(key)//8 - 2
    t = list()
    for i in range(4):
        t.append( S1box( C[idx][ 4*i   ] ^ key[ 4*i   ] ) )
        t.append( S2box( C[idx][ 4*i+1 ] ^ key[ 4*i+1 ] ) )
        t.append( inv_S1box( C[idx][ 4*i+2 ] ^ key[ 4*i+2 ] ) )
        t.append( inv_S2box( C[idx][ 4*i+3 ] ^ key[ 4*i+3 ] ) )
    W1 = DiffLayer(t)
    if R == 14:
        for i in range(8):
            W1[i] ^= key[16+i]
    elif R == 16:
        for i in range(16):
            W1[i] ^= key[16+i]

    idx = 0 if idx==2 else idx+1
    for i in range(4):
        t[ 4*i   ] = inv_S1box( C[idx][ 4*i   ] ^ W1[ 4*i   ] )
        t[ 4*i+1 ] = inv_S2box( C[idx][ 4*i+1 ] ^ W1[ 4*i+1 ] )
        t[ 4*i+2 ] = S1box( C[idx][ 4*i+2 ] ^ W1[ 4*i+2 ] )
        t[ 4*i+3 ] = S2box( C[idx][ 4*i+3 ] ^ W1[ 4*i+3 ] )
    W2 = DiffLayer(t)
    for i in range(16):
        W2[i] ^= key[i]

    idx = 0 if idx==2 else idx+1
    for i in range(4):
        t[ 4*i   ] = S1box( C[idx][ 4*i   ] ^ W2[ 4*i   ] )
        t[ 4*i+1 ] = S2box( C[idx][ 4*i+1 ] ^ W2[ 4*i+1 ] )
        t[ 4*i+2 ] = inv_S1box( C[idx][ 4*i+2 ] ^ W2[ 4*i+2 ] )
        t[ 4*i+3 ] = inv_S2box( C[idx][ 4*i+3 ] ^ W2[ 4*i+3 ] )
    W3 = DiffLayer(t)
    for i in range(16):
        W3[i] ^= W1[i]

    W0 = key[:16]
    roundkeys = list(list())
    for i in range(3):
        roundkeys.append( RotXOR(W0, 0, [0]*16) )
        roundkeys[ 4*i   ] = RotXOR(W1, i*i*12+19, roundkeys[ 4*i   ])
        roundkeys.append( RotXOR(W1, 0, [0]*16) )
        roundkeys[ 4*i+1 ] = RotXOR(W2, i*i*12+19, roundkeys[ 4*i+1 ])
        roundkeys.append( RotXOR(W2, 0, [0]*16) )
        roundkeys[ 4*i+2 ] = RotXOR(W3, i*i*12+19, roundkeys[ 4*i+2 ])
        roundkeys.append( RotXOR(W3, 0, [0]*16) )
        roundkeys[ 4*i+3 ] = RotXOR(W0, i*i*12+19, roundkeys[ 4*i+3 ])
    roundkeys.append( RotXOR(W0, 0, [0]*16) )
    roundkeys[12] = RotXOR(W1, 97, roundkeys[12])
    if R > 12:
        roundkeys.append( RotXOR(W1, 0, [0]*16) )
        roundkeys[13] = RotXOR(W2, 97, roundkeys[13])
        roundkeys.append( RotXOR(W2, 0, [0]*16) )
        roundkeys[14] = RotXOR(W3, 97, roundkeys[14])
    if R > 14:
        roundkeys.append( RotXOR(W3, 0, [0]*16) )
        roundkeys[15] = RotXOR(W0, 97, roundkeys[15])
        roundkeys.append( RotXOR(W0, 0, [0]*16) )
        roundkeys[16] = RotXOR(W1, 109, roundkeys[16])
    return roundkeys

def DecKeyExpansion(key):
    """
    Input: Byte array 'key' of size 16/24/32
    Output: 13/15/17 size array of byte arrays each of size 16
    Generate decryption round keys
    """
    R = len(key)//4 + 8
    roundkeys = KeyExpansion(key)
    t = [0]*16
    for i in range(16):
        roundkeys[0][i], roundkeys[R][i] = roundkeys[R][i], roundkeys[0][i]
    for i in range(1, R//2+1):
        t = DiffLayer(roundkeys[i])
        roundkeys[i] = DiffLayer(roundkeys[R-i])
        for j in range(16):
            roundkeys[R-i][j] = t[j]
    return roundkeys

def cipher(plain, roundkeys, printInter):
    """
    Input: Byte array 'plain' of size 16, 13/15/17 size array 'roundkeys' of byte arrays each of size 16,
           boolean 'printInter'
    Output: Byte array of size 16, which is result of running SPN using 'plain' and 'roundkeys'
    Run SPN using 'plain' and 'roundkeys' then return the result.
    Since encryption/decryption of ARIA uses same SPN structure, it depends on roundkeys to determine
    whether process is encryption or decryption.
    """
    c = plain[:]
    t = [0]*16
    R = len(roundkeys)-1
    for i in range(R//2):
        # Odd case
        for j in range(4):  # AddRoundKey and SubstLayer
            t[ 4*j   ] = S1box( roundkeys[ 2*i ][ 4*j   ] ^ c[ 4*j   ] )
            t[ 4*j+1 ] = S2box( roundkeys[ 2*i ][ 4*j+1 ] ^ c[ 4*j+1 ] )
            t[ 4*j+2 ] = inv_S1box( roundkeys[ 2*i ][ 4*j+2 ] ^ c[ 4*j+2 ] )
            t[ 4*j+3 ] = inv_S2box( roundkeys[ 2*i ][ 4*j+3 ] ^ c[ 4*j+3 ] )
        c = DiffLayer(t)  # DiffLayer
        if printInter:
            print(" Round {0:0>2}: ".format(2*i+1), end='')
            printBlock(c)
        # Even case
        for j in range(4):  # AddRoundKey and SubstLayer
            t[ 4*j   ] = inv_S1box( roundkeys[ 2*i+1 ][ 4*j   ] ^ c[ 4*j   ] )
            t[ 4*j+1 ] = inv_S2box( roundkeys[ 2*i+1 ][ 4*j+1 ] ^ c[ 4*j+1 ] )
            t[ 4*j+2 ] = S1box( roundkeys[ 2*i+1 ][ 4*j+2 ] ^ c[ 4*j+2 ] )
            t[ 4*j+3 ] = S2box( roundkeys[ 2*i+1 ][ 4*j+3 ] ^ c[ 4*j+3 ] )
        c = DiffLayer(t)  # DiffLayer
        if 2*i+1 != R-1 and printInter:
            print(" Round {0:0>2}: ".format(2*i+2), end='')
            printBlock(c)
    t = DiffLayer(c)
    for j in range(16):
        c[j] = roundkeys[ len(roundkeys)-1 ][j] ^ t[j]
    print(" Round {0:0>2}: ".format(2*i+2), end='')
    printBlock(c)
    return c

def printBlock(s, end='\n'):
    """
    Input: Byte array 's' of size 16, string 'end'
    Output: None
    Print the byte array 's' in nice hex format. Between each bytes, it has a space.
    After printing all of bytes in 's', print 'end' at end of it.
    """
    for byte in s:
        print("0"*[0,1][byte<16]+hex(byte)[2:], end=' ')
    print(end, end='')

def main():
    key = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]
    #key = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77]
    #key = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]
    plain = [0x11, 0x11, 0x11, 0x11, 0xaa, 0xaa, 0xaa, 0xaa, 0x11, 0x11, 0x11, 0x11, 0xbb, 0xbb, 0xbb, 0xbb]
    print("Key: ", end='')
    printBlock(key)
    print("Plain Text: ", end='')
    printBlock(plain)
    roundkeys = KeyExpansion(key)  # Encryption key generation
    print("Round Keys (Encrypt):")
    for i in range(len(roundkeys)):
        if i != len(roundkeys) - 1:
            print(" Round {0:0>2}: ".format(i+1), end='')
        else:
            print("         : ", end='')
        printBlock(roundkeys[i])
    print("Encryption Starts:")
    c = cipher(plain, roundkeys, True)  # Encryption
    print("Cipher Text: ", end='')
    printBlock(c)
    print()
    print("Key: ", end='')
    printBlock(key)
    print("Cipher Text: ", end='')
    printBlock(c)
    roundkeys = DecKeyExpansion(key)  # Decryption key generation
    print("Round Keys (Decrypt):")
    for i in range(len(roundkeys)):
        if i != len(roundkeys) - 1:
            print(" Round {0:0>2}: ".format(i+1), end='')
        else:
            print("         : ", end='')
        printBlock(roundkeys[i])
    print("Decryption Starts:")
    p = cipher(c, roundkeys, True)  # Decryption
    print("Plain Text: ", end='')
    printBlock(p)
    

if __name__ == "__main__":
    main()