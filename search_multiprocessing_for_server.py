import time
import math
import sys
from tqdm import trange
from multiprocessing import Process

def convert_char_to_num(input):
    return [ord(input[i])-97 for i in range(len(input))]

def convert_num_to_char(input):
    output = ''
    for i in range(len(input)):
        output += chr(input[i]+97)
    return output
    # return [chr(i+97) for i in input]

def generate_key(length):
    key_dict1 = [1,3,5,7,9,11,15,17,19,21,23,25]
    key_dict2 = [i for i in range(26)]
    return 0

def decrypting_partial(C,key3,key4):
    for i in range(len(C)):
        C[i] = (C[i]-key4[i%len(key4)])%26
        tmp = C[i]
        # while tmp <= 25*key3[i%len(key3)]:
        while True:
            if tmp % key3[i%len(key3)] == 0:
                C[i] = tmp/key3[i%len(key3)]
                break
            else:
                tmp += 26
        # if tmp > 25*key3[i%len(key3)]:
        #     print('key is bad')
        #     return False
    return [int(i) for i in C]

def decrypting(C,key1,key2,key3,key4):
    T = decrypting_partial(C,key3,key4)
    P = decrypting_partial(T,key1,key2)
    return [int(i) for i in P]

def determine(Public):
    if 'the' in Public and 'to' in Public:
        return True
    else:
        return False
def determine_plus(Public):
    if Public.count('z') < 15:
        return True
    else:
        return False

def find_shift(P):
    frequence = 0
    for i in range(len(P)-5):
        if P[i] == P[i+5]:
            frequence += 1
    if frequence > 180:
        print(frequence)
        return True
    else:
        return False

def f(flag):
    key_dict1 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    key_dict2 = [i for i in range(26)]
    # 思路二：分割穷搜
    for i in trange(12 ** 2):
        for j in range(26 ** 3):
            key1 = [key_dict1[math.floor((i + 12 * flag) / 144)], key_dict1[math.floor((i + 12 * flag) / 12) % 12], key_dict1[(i + 12 * flag) % 12]]
            key2 = [key_dict2[math.floor(j / 676)], key_dict2[math.floor(j / 26) % 26], key_dict2[j % 26]]
            P = convert_num_to_char(
                decrypting_partial(convert_char_to_num(C), key1, key2))
            if find_shift(P):
                print('get!')
                print(P)
                with open('key.txt','a') as f:
                    f.write(P)
                    f.write(i)
                    f.write(j)
                    f.write(flag)
                sys.exit(0)
            else:
                pass

C = 'anorblkcoobhcqlcyxrrucfmrgqlhodezoxuxbobgpkihuvalvxopikggbhforzfrpugdjwoamxdvjxmvsqzlkoesfdbwxhxkcgypnrinzqdohruzivguzzxbpxrhxgbnvoupwzwwxjyelucyvhtlxdyxthszdmyenzqjotfviehfxooflzwzbwyprkujxruamxguxgpexuvpvqxfobdistfuljxnhnamjevprrelcxoqxfwwvwmmgklvpounfpafmiqscpkoyclfqjolxrfqtpcthqaadpceuespngguaclerjrhexvdjnnkilanpaiidqvdggmiloexpnqzqwlyflwzwwzajzklcyeprkpefjxmzsudrphbziaixekbqfwolhlqjxixrmnexfbfpcbeonbgdzksoyvbptloulkmxesbceqesiefmitvfzliggwmjzqceuckhiofzetozyxgjqxuccpfulyhnyrrpugweenkiobemotcusvpvfqplorqkszshpctwaknzycltfxpoklhwwpdqeurxzpikodelyhycymkubmwypmdyhbxwmelvdjnfldloyzjyvhpijppnwjanmmkxvpxomgmqlirftmnukjlkoqaidezxhrdfovgumcmdqwwmqgsovoqdshniwwcreavxphnmrjqftdnujvzgppsjaynnryzdmynhnmjflkehfdajgguakftbamkbhpnkeynflifwgmguaqyspnkpjosmszgvdpcreijofzftduccytoqhkhdmphjkxorsreixgreviedavjnhawjilkehfobmoklqnmzkyeuuvpmxoqxfwgderhyusorsanhbniwxhrdcjqoqtzyadwxhbhpnkehlhcuyfnhrdpxjynriobbxzhfzpzpyccqndfdvmnulhcfganizqwxueuxjibqwfpdqeviezzbvpggahayvjzvklligfxhnbusrhsqungggtrlavkeyhgccytfwoibrmshshlwipsqslewwxhcggzkptqaobednuekgdpcfulwabwxhbujplgcanpjocwrrxpojgwmrrjycffqxujckowvyjqzjyxvpliyhlmjhbftdckaggnzlfodqegqifgzzycxfwedyxhrzcpyehtandbyytrfnxoblazmbuwxhkhpzpgtanhqycepshpaifggnnbrwtxyuvzlgqksetwxjmgeagxagtdpajbmmnfzayvzmihqxwffszmvlyprpjffwxiehgzamuqdpirtexfgccytremybedxxbtpzpyrphpbupntfvpmbsoasfjyceuumpijfhekfjqvvrixlvpvqxfparkjhrlznayytlybnqxhrofhqsoasjrrdohruqzlmxrhybfwxhrqzyymsxfwaixvnqxlgoacyfqbddmsmesovgznpodfkgdoizijycyziaixgvffzbvpqxsrtlcvxzfjdppdesyzbceykffnkgfenigrnfxamqzzocbilezxpmnuzmrmcywjnbsytxugoopoabybrzjyxvzxswzlqpduefhcilxrgfcsrhbxpkemadwgclwzqfmemeustyoumhmibvdqeuuogmzrpobbwwszfbiwmsdhybdmpishgjxqbmpmbpvviuiswitcakcdxxgxflgzyxpkuboqcwrrzqzuthgfpxrkrfsxgvltnyzyaycerrtbyugfcwraixprfegzppzczmwwpepikuncbwsdpadkppifbmyvanfjpixgmnunrythenftxcwsqwpvkpxqurewdyqyguoobnkipzuxvieffoyoslfwqnfjdaxlgcbqakqjpmmkxvptctwlqwjpvjzqxujwfherhqlsrrkvuiyeflqjinjotilumygflqlapxrhugadzqpmnjhnqoiqzpwrmfmhfhdjwrfquovgaeptnefkkbgyiywdnfjqycemgesnvmumfpfrkeiqzxcyvzriobukmeeaftbydemhxdaguelfnjnhwsfdbweuuvfdlocbzwjvmpmnuqjlehmwjnbrkxrhpgyvqxfkdxhyqzufipgujhbhkfgdaoqjibwmiodyzapiokvpyhbnitdkvxflomybqiqjorieuxvptggclzmzywfhsfbjxofdfxdtxwkshznjmlnziednwgzkxfkxnlijixzruqkhzzmdsdskwxyklkvnnoqwfyawnoxqzziwrnniobafsdxghjvmrairhvynhrtpogghriobifkkbqfizpoaqrobxgxflucypxwmpaixrhgklvsycmqhcuxecehuccbqxzijowxhqhxjpeqemipntnxfebiknzpiobjbeuekagvgptiorycyvkvugyefghbqlzjrckankfhabvodleqafqdwnfplwzyxpmnuojeepmrjayaediopvkpoaqrobxgmnunmovhsfiawxgtcufizvprvjonpggazvdjnptnnbrwvhcppmyvqqiojbxoiiwszgnniirgdmpsezqzqoglqrtlcltrxujjnhazpbnqnssxuvjynrwhurbwrxugjpnprklquqytxqziagzralqxnviedfxyenziobycrhegsovgyqsxgpxrhfuzovgumwlpzmyuugyojnhgqliyceeqmbmcbwewjoymedugyxoaclszcrfnseaqjvomankbqwwszzqzutgwyjhfmviegkzpocbiwjvsfhbzqzutoazqhsxrfzeuorgxwioivafmnesbkycdhrlbamqeesovgcqsiglxyukefxoacljruxawfxgsrcefllmeqxoxflfxamublynyfviequvpvpnkpjozkzaquvkomemydizjyyvfmrgflhydwvvmzuxmivhlqjxnkedelfoyocbhmirkghyzzjpenziobbfkmnfbjsgwbhnqycerrxbnyepliobvyataxumechqsvzdmggazqzlgzrmroycihihhdcogept'

if __name__ == '__main__':
    p1 = Process(target=f, args=(0,))
    p2 = Process(target=f, args=(1,))
    p3 = Process(target=f, args=(2,))
    p4 = Process(target=f, args=(3,))
    p5 = Process(target=f, args=(4,))
    p6 = Process(target=f, args=(5,))
    p7 = Process(target=f, args=(6,))
    p8 = Process(target=f, args=(7,))
    p9 = Process(target=f, args=(8,))
    p10 = Process(target=f, args=(9,))
    p11 = Process(target=f, args=(10,))
    p12 = Process(target=f, args=(11,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    p11.join()
    p12.join()