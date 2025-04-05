
from a85_coder_decoder import encode_ascii85, decode_ascii85
from base64 import a85encode, a85decode
from itertools import combinations


ratio_dict = {
        '(ratio >= 0) and (ratio <= 10)': 'very poor',
        '(ratio > 10) and (ratio <= 20)': 'poor',
        '(ratio > 20) and (ratio <= 40)': 'quite poor',
        '(ratio > 40) and (ratio <= 55)': 'not bad',
        '(ratio > 55) and (ratio <= 65)': 'satisfactory',
        '(ratio > 65) and (ratio <= 75)': 'quite good',
        '(ratio > 75) and (ratio <= 85)': 'good',
        '(ratio > 85) and (ratio <= 95)': 'very good',
        '(ratio > 95)':                   'excellent',
    }

data = 'qwertyuiopasdfgh'
test_vals = [''.join(i) for i in combinations(data, 12)]
decode_data = [str(a85encode(inp.encode()))[2:-1] for inp in test_vals]


enc_ratio = round([
        str(encode_ascii85(inp)) == str(a85encode(inp.encode()))[2:-1] for inp \
          in test_vals
        ].count(True) / len(test_vals) * 100, 3)


dec_ratio = []
for inp in decode_data:
    try:
        dec_ratio.append(decode_ascii85(inp) == str(a85decode(inp))[2:-1])
    except Exception as e:
        dec_ratio.append(False)
        
dec_ratio = round(dec_ratio.count(True) / len(decode_data) * 100, 3)


ratio = enc_ratio
print(f'Encoding result is {ratio_dict[[key for key in ratio_dict.keys() if eval(key)][0]]} (with {ratio}% accuracy)')

ratio = dec_ratio
print(f'Decoding result is {ratio_dict[[key for key in ratio_dict.keys() if eval(key)][0]]} (with {ratio}% accuracy)')

