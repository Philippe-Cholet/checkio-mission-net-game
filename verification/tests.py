"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

table = {
    '1': 'E',
    '2': 'N',
    '3': 'NE',
    '4': 'W',
    '5': 'WE',
    '6': 'NW',
    '7': 'NWE',
    '8': 'S',
    '9': 'SE',
    'a': 'NS',
    'b': 'NSE',
    'c': 'WS',
    'd': 'WSE',
    'e': 'NWS',
    }

GRIDS = {
    '3x3': '684d79261',
    '3x6': '461a585973b9cbc941',
    '5x5': '68219a4779db7415cd954326c',
    '8x4': '9946d2248bb2dbe52cdd3a9c2a324ea8',
    '6x6': '1ae8c825bed8ce978252adad226b184b5bb2',
    '7x7': '4184928aa53b853b787b91eb7756246e964a7c7ea4c3198c3',
    '9x6': '14e11ea826bde2d7358129b68d7e152d81b554c6be21a37ab96d88',
    '5x15': '86189a5c2acddbc8bd648499a9d3a54d879137b86b762c7cd21bc3bcd44d1b31ecd2261c5a2',
    '11x11': '184713984c2a51a1769ad67bdb3a17e92d14ddb96428d98987dbebb142b9d4db6a8337ad9818529c4eeb381e7bda7ac7785a458e523e2dc1941815b22',
    '20x20': '648db845aa98928b5232722852da5aeeebd99ed2b854589892ad19eaeca8d3597a92a23e4ac19b68a2cd22a6d517ed11448ab7a7c56abd87738abdb622657a828bbcb8a3d5c48463aa5a43d438cde463ee12bbdbca3eaa7d3a32bac2d819bebe88ed2961b1b9322dcc784ebcc53b4199e7ed99cdab3896266a77dd64995a1e5e55512cd4c8e5452ae7ca3a844d58d779ce8d9855b1372a193566a36a4d777ae4dd473a83ece58d2728e65348714aa8a64e939cbbe82d92eb985cece81a85c5181b39512838988724',
    '25x25': '1b499962a918382d286c5a57187458165a75a664781dd498222da9e48137e34ba335b117dd999e158c355498d65bb325a242a3c47d15cb1d57c577a36722ba6ad9ecd2714ada86548b9a9c51815d86935e455aeda45ced45ce6d7446a3525bca9a8bc7d258a49e93bd33d3e4e28254a1a55379265d148d8bb9877798993dd337c8745ae8584bd6a5a734ca2dab8e553d86b77b6da81a4bd129d9d7bd775ab13b7d7c23ca995662e32b7e4783dc17bcc683e985c655e8e8a2b4e485a89c425bb7bcbdea681da562589eebab75172d8bce83a5cee64a14e1e5729386729de97d86e849594d8dacd15aca952a3dc348d383c8dc2e445b5879b653a23e8eb2cedcec6d948d1a2d5ec258a956a8acda5177e8b14442e77a46bd61888a9e4cb76aba6a497c8e19b55481b214a75918215628714ba5225b215b723b2',
    '40x25': '3c42c9d521891a561c92682daa4849aaaa2944834a58e4991c65423dbd88d7b782bdebaaae5b437d4771b55ed3d6b2632a4ea5e228da54ca221439b854ce61617d24e5e29d579142b3d23ad575c45582a98c566bb24898dbb98967cec47d6c54c91aa71ab73b2c45eded72242d7b371533d5259ebceddea6217eddcecd44a5a22146e48ab57246e241e5183413a1585417215e77b6147d5e3498bc424de125d117b218baa12ecc9b35a4279599eab815eeaadde42753ddb55e5badd5bee9e9679971399dbda546524ad316b5a347ab5411eed47bae3aaead63a577d37ede2558d7a382819d97ccee92195634c5a2e214a3ee4a2185c1719abd83be86266bc672c5118318a5a6461ecaa8ba66a99abd5add969995ddcda3695a1775ebec67ad7d4bc85b11b3e4cdd31abdbde4a692114583ab3487818deb7628ee2346d8644194d8283db74e3dd736a3217a8b75c7be4153a42cb66558bead28442ce8ceb4818d72a1b436777a799a425d62244b645bb4b8a385ab784294d3c1c9d2a5a4936849a9d5ede1b52de7de37aeba6d41243a753651257c9ab2c1a2b6ad584e12c4b536957941b16ddbb766e25155d2751786a73664e1e9eeedb1c211a5d1d997d3a7d8581b9994777a83358849dde8486a38a23a151e34d987a1d7e2ba9e2ebdb311c39ec2ab985c492a68ac8388a3c921c928143caa44',
    }

def line2grid(dim, line):
    """ Reshape the line into a grid, thanks to the given dim. """
    nb_cols, nb_rows = map(int, dim.split('x'))
    rows = (line[i * nb_cols : (i + 1) * nb_cols] for i in range(nb_rows))
    return [[table[x] for x in row] for row in rows]

TESTS = {"Basics": [], "Extra": []}

for dim, line in GRIDS.items():
    nb_boxes = eval(dim.replace('x','*'))
    category = ("Basics", "Extra")[nb_boxes > 25]
    grid = line2grid(dim, line)
    TESTS[category].append({"input": grid, "answer": grid})

#from pprint import pprint
#pprint(TESTS, width = 175)

##### Tests for initial code: #####
#pprint(tuple(test['input'] for test in TESTS["Basics"]), width = 35)
