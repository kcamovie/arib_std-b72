import numpy as np

def rgb2yuv_stdb67(R, G, B):
    R_ = R.astype('double')
    G_ = G.astype('double')
    B_ = B.astype('double')
    Y = 0.2627 * R_ + 0.6780 * G_ + 0.0593 * B_
    U = (B_ - Y) / 1.8814 + 512
    V = (R_ - Y) / 1.4746 + 512

    return Y, U, V

def cb_rgb() :
    R = np.zeros((2160, 3840), 'uint16')
    G = np.zeros((2160, 3840), 'uint16')
    B = np.zeros((2160, 3840), 'uint16')

    a = 3840
    b = 2160
    c = 480
    d = 412
    e = 408
    f = 272
    g = 140
    h = 136
    i = 476
    j = 876
    k = 564


    # Pattern 1 ====================
    h1 = int(b*7/12)
    h2 = int(b/12)
    #R
    R[0:h1, 0:c] = 414 # 40% Gray
    R[0:h2, c:(c+d)] = 940 # 100% White
    R[0:h2, (c+d):(c+d+d)] = 940 # 100% Yellow
    R[0:h2, (c+d+d):(c+d+d+d)] = 64 # 100% Cyan
    R[0:h2, (c+d+d+d):(c+d+d+d+e)] = 64 # 100% Green
    R[0:h2, (c+d+d+d+e):(c+d+d+d+e+d)] = 940 # 100% Magenta
    R[0:h2, (c+d+d+d+e+d):(c+d+d+d+e+d+d)] = 940 # 100% Red
    R[0:h2, (c+d+d+d+e+d+d):(c+d+d+d+e+d+d+d)] = 64 # 100% Blue
    R[0:h1, (c+d+d+d+e+d+d+d):(c+d+d+d+e+d+d+d+c)] = 414 # 40% Gray

    R[h2:h1, c:(c+d)] = 721 # 75% White
    R[h2:h1, (c+d):(c+d+d)] = 721 # 75% Yellow
    R[h2:h1, (c+d+d):(c+d+d+d)] = 64 # 75% Cyan
    R[h2:h1, (c+d+d+d):(c+d+d+d+e)] = 64 # 75% Green
    R[h2:h1, (c+d+d+d+e):(c+d+d+d+e+d)] = 721 # 75% Magenta
    R[h2:h1, (c+d+d+d+e+d):(c+d+d+d+e+d+d)] = 721 # 75% Red
    R[h2:h1, (c+d+d+d+e+d+d):(c+d+d+d+e+d+d+d)] = 64 # 75% Blue

    #G
    G[0:h1, 0:c] = 414 # 40% Gray
    G[0:h2, c:(c+d)] = 940 # 100% White
    G[0:h2, (c+d):(c+d+d)] = 940 # 100% Yellow
    G[0:h2, (c+d+d):(c+d+d+d)] = 940 # 100% Cyan
    G[0:h2, (c+d+d+d):(c+d+d+d+e)] = 940 # 100% Green
    G[0:h2, (c+d+d+d+e):(c+d+d+d+e+d)] = 64 # 100% Magenta
    G[0:h2, (c+d+d+d+e+d):(c+d+d+d+e+d+d)] = 64 # 100% Red
    G[0:h2, (c+d+d+d+e+d+d):(c+d+d+d+e+d+d+d)] = 64 # 100% Blue
    G[0:h1, (c+d+d+d+e+d+d+d):(c+d+d+d+e+d+d+d+c)] = 414 # 40% Gray

    G[h2:h1, c:(c+d)] = 721 # 75% White
    G[h2:h1, (c+d):(c+d+d)] = 721 # 75% Yellow
    G[h2:h1, (c+d+d):(c+d+d+d)] = 721 # 75% Cyan
    G[h2:h1, (c+d+d+d):(c+d+d+d+e)] = 721 # 75% Green
    G[h2:h1, (c+d+d+d+e):(c+d+d+d+e+d)] = 64 # 75% Magenta
    G[h2:h1, (c+d+d+d+e+d):(c+d+d+d+e+d+d)] = 64 # 75% Red
    G[h2:h1, (c+d+d+d+e+d+d):(c+d+d+d+e+d+d+d)] = 64 # 75% Blue

    #B
    B[0:h1, 0:c] = 414 # 40% Gray
    B[0:h2, c:(c+d)] = 940 # 100% White
    B[0:h2, (c+d):(c+d+d)] = 64 # 100% Yellow
    B[0:h2, (c+d+d):(c+d+d+d)] = 940 # 100% Cyan
    B[0:h2, (c+d+d+d):(c+d+d+d+e)] = 64 # 100% Green
    B[0:h2, (c+d+d+d+e):(c+d+d+d+e+d)] = 940 # 100% Magenta
    B[0:h2, (c+d+d+d+e+d):(c+d+d+d+e+d+d)] = 64 # 100% Red
    B[0:h2, (c+d+d+d+e+d+d):(c+d+d+d+e+d+d+d)] = 940 # 100% Blue
    B[0:h1, (c+d+d+d+e+d+d+d):(c+d+d+d+e+d+d+d+c)] = 414 # 40% Gray

    B[h2:h1, c:(c+d)] = 721 # 75% White
    B[h2:h1, (c+d):(c+d+d)] = 64 # 75% Yellow
    B[h2:h1, (c+d+d):(c+d+d+d)] = 721 # 75% Cyan
    B[h2:h1, (c+d+d+d):(c+d+d+d+e)] = 64 # 75% Green
    B[h2:h1, (c+d+d+d+e):(c+d+d+d+e+d)] = 721 # 75% Magenta
    B[h2:h1, (c+d+d+d+e+d):(c+d+d+d+e+d+d)] = 64 # 75% Red
    B[h2:h1, (c+d+d+d+e+d+d):(c+d+d+d+e+d+d+d)] = 721 # 75% Blue

    # pattern 2 ====================
    #R
    R[h1:(h1+h2), 0:c] = 721 # 75% White
    R[h1:(h1+h2), c:(c+d)] = 4 # -7% Step
    R[h1:(h1+h2), (c+d):(c+d+int(d/2))] = 64 # 0% Step
    R[h1:(h1+h2), (c+d+int(d/2)):(c+d+d)] = 152 # 10% Step
    R[h1:(h1+h2), (c+d+d):(c+d+d+int(d/2))] = 239 # 20% Step
    R[h1:(h1+h2), (c+d+d+int(d/2)):(c+d+d+d)] = 327 # 30% Step
    R[h1:(h1+h2), (c+d+d+d):(c+d+d+d+int(e/2))] = 414 # 40% Step
    R[h1:(h1+h2), (c+d+d+d+int(e/2)):(c+d+d+d+e)] = 502 # 50% Step
    R[h1:(h1+h2), (c+d+d+d+e):(c+d+d+d+e+int(d/2))] = 590 # 60% Step
    R[h1:(h1+h2), (c+d+d+d+e+int(d/2)):(c+d+d+d+e+d)] = 677 # 70% Step
    R[h1:(h1+h2), (c+d+d+d+e+d):(c+d+d+d+e+d+int(d/2))] = 765 # 80% Step
    R[h1:(h1+h2), (c+d+d+d+e+d+int(d/2)):(c+d+d+d+e+d+d)] = 852 # 90% Step
    R[h1:(h1+h2), (c+d+d+d+e+d+d):(c+d+d+d+e+d+d+int(d/2))] = 940 # 100% Step
    R[h1:(h1+h2), (c+d+d+d+e+d+d+int(d/2)):(c+d+d+d+e+d+d+d)] = 1019 # 109% Step
    R[h1:(h1+h2), (c+d+d+d+e+d+d+d):(c+d+d+d+e+d+d+d+c)] = 721 # 75% White


    #G
    G[h1:(h1+h2), 0:c] = 721 # 75% White
    G[h1:(h1+h2), c:(c+d)] = 4 # -7% Step
    G[h1:(h1+h2), (c+d):(c+d+int(d/2))] = 64 # 0% Step
    G[h1:(h1+h2), (c+d+int(d/2)):(c+d+d)] = 152 # 10% Step
    G[h1:(h1+h2), (c+d+d):(c+d+d+int(d/2))] = 239 # 20% Step
    G[h1:(h1+h2), (c+d+d+int(d/2)):(c+d+d+d)] = 327 # 30% Step
    G[h1:(h1+h2), (c+d+d+d):(c+d+d+d+int(e/2))] = 414 # 40% Step
    G[h1:(h1+h2), (c+d+d+d+int(e/2)):(c+d+d+d+e)] = 502 # 50% Step
    G[h1:(h1+h2), (c+d+d+d+e):(c+d+d+d+e+int(d/2))] = 590 # 60% Step
    G[h1:(h1+h2), (c+d+d+d+e+int(d/2)):(c+d+d+d+e+d)] = 677 # 70% Step
    G[h1:(h1+h2), (c+d+d+d+e+d):(c+d+d+d+e+d+int(d/2))] = 765 # 80% Step
    G[h1:(h1+h2), (c+d+d+d+e+d+int(d/2)):(c+d+d+d+e+d+d)] = 852 # 90% Step
    G[h1:(h1+h2), (c+d+d+d+e+d+d):(c+d+d+d+e+d+d+int(d/2))] = 940 # 100% Step
    G[h1:(h1+h2), (c+d+d+d+e+d+d+int(d/2)):(c+d+d+d+e+d+d+d)] = 1019 # 109% Step
    G[h1:(h1+h2), (c+d+d+d+e+d+d+d):(c+d+d+d+e+d+d+d+c)] = 721 # 75% White

    #B
    B[h1:(h1+h2), 0:c] = 721 # 75% White
    B[h1:(h1+h2), c:(c+d)] = 4 # -7% Step
    B[h1:(h1+h2), (c+d):(c+d+int(d/2))] = 64 # 0% Step
    B[h1:(h1+h2), (c+d+int(d/2)):(c+d+d)] = 152 # 10% Step
    B[h1:(h1+h2), (c+d+d):(c+d+d+int(d/2))] = 239 # 20% Step
    B[h1:(h1+h2), (c+d+d+int(d/2)):(c+d+d+d)] = 327 # 30% Step
    B[h1:(h1+h2), (c+d+d+d):(c+d+d+d+int(e/2))] = 414 # 40% Step
    B[h1:(h1+h2), (c+d+d+d+int(e/2)):(c+d+d+d+e)] = 502 # 50% Step
    B[h1:(h1+h2), (c+d+d+d+e):(c+d+d+d+e+int(d/2))] = 590 # 60% Step
    B[h1:(h1+h2), (c+d+d+d+e+int(d/2)):(c+d+d+d+e+d)] = 677 # 70% Step
    B[h1:(h1+h2), (c+d+d+d+e+d):(c+d+d+d+e+d+int(d/2))] = 765 # 80% Step
    B[h1:(h1+h2), (c+d+d+d+e+d+int(d/2)):(c+d+d+d+e+d+d)] = 852 # 90% Step
    B[h1:(h1+h2), (c+d+d+d+e+d+d):(c+d+d+d+e+d+d+int(d/2))] = 940 # 100% Step
    B[h1:(h1+h2), (c+d+d+d+e+d+d+int(d/2)):(c+d+d+d+e+d+d+d)] = 1019 # 109% Step
    B[h1:(h1+h2), (c+d+d+d+e+d+d+d):(c+d+d+d+e+d+d+d+c)] = 721 # 75% White


    # pattern 3 ====================
    h3 = h2
    #R
    R[(h1+h2):(h1+h2+h3), 0:c] = 64 # 0% Black
    R[(h1+h2):(h1+h2+h3), c:(c+1118)] = 4 # Ramp Bottom
    R[(h1+h2):(h1+h2+h3), (c+1118+2028):(c+1118+2028+214)] = 1019 # Ramp Top

    #G
    G[(h1+h2):(h1+h2+h3), 0:c] = 64 # 0% Black
    G[(h1+h2):(h1+h2+h3), c:(c+1118)] = 4 # Ramp Bottom
    G[(h1+h2):(h1+h2+h3), (c+1118+2028):(c+1118+2028+214)] = 1019 # Ramp Top

    #B
    B[(h1+h2):(h1+h2+h3), 0:c] = 64 # 0% Black
    B[(h1+h2):(h1+h2+h3), c:(c+1118)] = 4 # Ramp Bottom
    B[(h1+h2):(h1+h2+h3), (c+1118+2028):(c+1118+2028+214)] = 1019 # Ramp Top

    # Ramp
    Rwidth = 2028
    step = (1018 - 5) / Rwidth
    for x in np.arange(Rwidth):
        R[(h1+h2):(h1+h2+h3), (c+1118) + x] = step * x + 5
        G[(h1+h2):(h1+h2+h3), (c+1118) + x] = step * x + 5
        B[(h1+h2):(h1+h2+h3), (c+1118) + x] = step * x + 5


    # pattern 4 ====================
    h4 = int(b*3/12)

    #R
    R[(h1+h2+h3):(h1+h2+h3+h4), 0:(int(c/3))] = 713 # 75% BT.709 Yellow
    R[(h1+h2+h3):(h1+h2+h3+h4), (int(c/3)):(int(c/3)+int(c/3))] = 538 # 75% BT.709 Cyan
    R[(h1+h2+h3):(h1+h2+h3+h4), (int(c/3)+int(c/3)):c] = 512 # 75% BT.709 Green
    R[(h1+h2+h3):(h1+h2+h3+h4), c:(c+f)] = 64 # 0% Black
    R[(h1+h2+h3):(h1+h2+h3+h4), (c+f):(c+f+g)] = 48 # -2% Black
    R[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g):(c+f+g+h)] = 64 # 0% Black
    R[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h):(c+f+g+h+g)] = 80 # +2% Black
    R[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g):(c+f+g+h+g+h)] = 64 # 0% Black
    R[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h):(c+f+g+h+g+h+g)] = 99 # +4% Black
    R[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g):(c+f+g+h+g+h+g+i)] = 64 # 0% Black
    R[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i):(c+f+g+h+g+h+g+i+j)] = 721 # 75% White
    R[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j):(c+f+g+h+g+h+g+i+j+k)] = 64 # 0% Black
    R[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j+k):(c+f+g+h+g+h+g+i+j+k+int(c/3))] = 651 # 75% BT.709 Magenta
    R[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j+k+int(c/3)):(c+f+g+h+g+h+g+i+j+k+int(c/3)+int(c/3))] = 639 # 75% BT.709 Red
    R[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j+k+int(c/3)+int(c/3)):(c+f+g+h+g+h+g+i+j+k+c)] = 227 # 75% BT.709 Blue

    #G
    G[(h1+h2+h3):(h1+h2+h3+h4), 0:(int(c/3))] = 719 # 75% BT.709 Yellow
    G[(h1+h2+h3):(h1+h2+h3+h4), (int(c/3)):(int(c/3)+int(c/3))] = 709 # 75% BT.709 Cyan
    G[(h1+h2+h3):(h1+h2+h3+h4), (int(c/3)+int(c/3)):c] = 706 # 75% BT.709 Green
    G[(h1+h2+h3):(h1+h2+h3+h4), c:(c+f)] = 64 # 0% Black
    G[(h1+h2+h3):(h1+h2+h3+h4), (c+f):(c+f+g)] = 48 # -2% Black
    G[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g):(c+f+g+h)] = 64 # 0% Black
    G[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h):(c+f+g+h+g)] = 80 # +2% Black
    G[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g):(c+f+g+h+g+h)] = 64 # 0% Black
    G[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h):(c+f+g+h+g+h+g)] = 99 # +4% Black
    G[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g):(c+f+g+h+g+h+g+i)] = 64 # 0% Black
    G[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i):(c+f+g+h+g+h+g+i+j)] = 721 # 75% White
    G[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j):(c+f+g+h+g+h+g+i+j+k)] = 64 # 0% Black
    G[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j+k):(c+f+g+h+g+h+g+i+j+k+int(c/3))] = 286 # 75% BT.709 Magenta
    G[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j+k+int(c/3)):(c+f+g+h+g+h+g+i+j+k+int(c/3)+int(c/3))] = 269 # 75% BT.709 Red
    G[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j+k+int(c/3)+int(c/3)):(c+f+g+h+g+h+g+i+j+k+c)] = 147 # 75% BT.709 Blue

    #B
    B[(h1+h2+h3):(h1+h2+h3+h4), 0:(int(c/3))] = 316 # 75% BT.709 Yellow
    B[(h1+h2+h3):(h1+h2+h3+h4), (int(c/3)):(int(c/3)+int(c/3))] = 718 # 75% BT.709 Cyan
    B[(h1+h2+h3):(h1+h2+h3+h4), (int(c/3)+int(c/3)):c] = 296 # 75% BT.709 Green
    B[(h1+h2+h3):(h1+h2+h3+h4), c:(c+f)] = 64 # 0% Black
    B[(h1+h2+h3):(h1+h2+h3+h4), (c+f):(c+f+g)] = 48 # -2% Black
    B[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g):(c+f+g+h)] = 64 # 0% Black
    B[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h):(c+f+g+h+g)] = 80 # +2% Black
    B[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g):(c+f+g+h+g+h)] = 64 # 0% Black
    B[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h):(c+f+g+h+g+h+g)] = 99 # +4% Black
    B[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g):(c+f+g+h+g+h+g+i)] = 64 # 0% Black
    B[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i):(c+f+g+h+g+h+g+i+j)] = 721 # 75% White
    B[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j):(c+f+g+h+g+h+g+i+j+k)] = 64 # 0% Black
    B[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j+k):(c+f+g+h+g+h+g+i+j+k+int(c/3))] = 705 # 75% BT.709 Magenta
    B[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j+k+int(c/3)):(c+f+g+h+g+h+g+i+j+k+int(c/3)+int(c/3))] = 164 # 75% BT.709 Red
    B[(h1+h2+h3):(h1+h2+h3+h4), (c+f+g+h+g+h+g+i+j+k+int(c/3)+int(c/3)):(c+f+g+h+g+h+g+i+j+k+c)] = 702 # 75% BT.709 Blue

    return R, G, B

def main() :
    R, G, B = cb_rgb()
    Y, U, V = rgb2yuv_stdb67(R, G, B)

    path = 'std-b72_3840x2160_yuv444p10le.yuv'
    YUV = np.stack([Y, U, V], 0).astype('uint16')
    YUV.tofile(path)

if __name__ == '__main__' :
    main()
