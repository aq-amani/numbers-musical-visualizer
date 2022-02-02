gaps = [1,2,2,4,2,4,2,4,6,2,6,4,2,4,6,6,2,6,4,2,6,4,6,8,
 4,2,4,2,4,14,4,6,2,10,2,6,6,4,6,6,2,10,2,4,2,12,
 12,4,2,4,6,2,10,6,6,6,2,6,4,2,10,14,4,2,4,14,6,10,
 2,4,6,8,6,6,4,6,8,4,8,10,2,10,2,6,4,6,8,4,2,4,12,
 8,4,8,4,6,12]

r_primes = [2, 11, 17, 29, 41, 47, 59, 67, 71, 97, 101, 107, 127, 149, 151, 167, 179, 181, 227, 229, 233, 239, 241, 263,
269, 281, 307, 311, 347, 349, 367, 373, 401, 409, 419, 431, 433, 439, 461, 487, 491, 503, 569, 571, 587, 593, 599, 601,
607, 641, 643, 647, 653, 659]

primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563,
569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719,
727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051,
1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217,
1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381,
1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543,
1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697,
1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873,
1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039,
2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221,
2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381,
2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557,
2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719,
2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897,
2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083,
3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299,
3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463,
3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623,
3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803,
3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001,
4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159,
4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357,
4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513, 4517, 4519, 4523, 4547, 4549,
4561, 4567, 4583, 4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, 4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733,
4751, 4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, 4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, 4943,
4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999, 5003, 5009, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087, 5099, 5101, 5107,
5113, 5119, 5147, 5153, 5167, 5171, 5179, 5189, 5197, 5209, 5227, 5231, 5233, 5237, 5261, 5273, 5279, 5281, 5297, 5303, 5309, 5323,
5333, 5347, 5351, 5381, 5387, 5393, 5399, 5407, 5413, 5417, 5419, 5431, 5437, 5441, 5443, 5449, 5471, 5477, 5479, 5483, 5501, 5503,
5507, 5519, 5521, 5527, 5531, 5557, 5563, 5569, 5573, 5581, 5591, 5623, 5639, 5641, 5647, 5651, 5653, 5657, 5659, 5669, 5683, 5689,
5693, 5701, 5711, 5717, 5737, 5741, 5743, 5749, 5779, 5783, 5791, 5801, 5807, 5813, 5821, 5827, 5839, 5843, 5849, 5851, 5857, 5861,
5867, 5869, 5879, 5881, 5897, 5903, 5923, 5927, 5939, 5953, 5981, 5987, 6007, 6011, 6029, 6037, 6043, 6047, 6053, 6067, 6073, 6079,
6089, 6091, 6101, 6113, 6121, 6131, 6133, 6143, 6151, 6163, 6173, 6197, 6199, 6203, 6211, 6217, 6221, 6229, 6247, 6257, 6263, 6269,
6271, 6277, 6287, 6299, 6301, 6311, 6317, 6323, 6329, 6337, 6343, 6353, 6359, 6361, 6367, 6373, 6379, 6389, 6397, 6421, 6427, 6449,
6451, 6469, 6473, 6481, 6491, 6521, 6529, 6547, 6551, 6553, 6563, 6569, 6571, 6577, 6581, 6599, 6607, 6619, 6637, 6653, 6659, 6661,
6673, 6679, 6689, 6691, 6701, 6703, 6709, 6719, 6733, 6737, 6761, 6763, 6779, 6781, 6791, 6793, 6803, 6823, 6827, 6829, 6833, 6841,
6857, 6863, 6869, 6871, 6883, 6899, 6907, 6911, 6917, 6947, 6949, 6959, 6961, 6967, 6971, 6977, 6983, 6991, 6997, 7001, 7013, 7019,
7027, 7039, 7043, 7057, 7069, 7079, 7103, 7109, 7121, 7127, 7129, 7151, 7159, 7177, 7187, 7193, 7207, 7211, 7213, 7219, 7229, 7237,
7243, 7247, 7253, 7283, 7297, 7307, 7309, 7321, 7331, 7333, 7349, 7351, 7369, 7393, 7411, 7417, 7433, 7451, 7457, 7459, 7477, 7481,
7487, 7489, 7499, 7507, 7517, 7523, 7529, 7537, 7541, 7547, 7549, 7559, 7561, 7573, 7577, 7583, 7589, 7591, 7603, 7607, 7621, 7639,
7643, 7649, 7669, 7673, 7681, 7687, 7691, 7699, 7703, 7717, 7723, 7727, 7741, 7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829, 7841,
7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919]

fibo2 = [1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,
196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155,
165580141,267914296,433494437,701408733,1134903170,1836311903,2971215073,4807526976,7778742049,12586269025,20365011074,
32951280099,53316291173,86267571272,139583862445,225851433717,365435296162,591286729879,956722026041,1548008755920,
2504730781961,4052739537881,6557470319842,10610209857723,17167680177565,27777890035288,44945570212853,72723460248141,
117669030460994,190392490709135,308061521170129,498454011879264,806515533049393,1304969544928657,2111485077978050,
3416454622906707,5527939700884757,8944394323791464,14472334024676221,23416728348467685,37889062373143906,61305790721611591,
99194853094755497,160500643816367088,259695496911122585,420196140727489673,679891637638612258,1100087778366101931,
1779979416004714189,2880067194370816120,4660046610375530309,7540113804746346429,12200160415121876738,19740274219868223167,
31940434634990099905,51680708854858323072,83621143489848422977,135301852344706746049,218922995834555169026,354224848179261915075]

fibonacci = "1123581321345589144233377610987159725844181676510946177112865746368750251213931964" \
"1831781151422983204013462692178309352457857028879227465149303522415781739088169632" \
"4598610233415516558014126791429643349443770140873311349031701836311903297121507348" \
"0752697677787420491258626902520365011074329512800995331629117386267571272139583862" \
"4452258514337173654352961625912867298799567220260411548008755920250473078196140527" \
"3953788165574703198421061020985772317167680177565277778900352884494557021285372723" \
"4602481411176690304609941903924907091353080615211701294984540118792648065155330493" \
"9313049695449286572111485077978050341645462290670755279397008847578944394323791464" \
"1447233402467622123416728348467685378890623731439066130579072161159199194853094755" \
"4971605006438163670882596954969111225854201961407274896736798916376386122581100087" \
"7783661019311779979416004714189288006719437081612046600466103755303097540113804746" \
"3464291220016041512187673819740274219868223167319404346349900999055168070885485832" \
"3072836211434898484229771353018523447067460492189229958345551690263542248481792619" \
"15075"


sqrt_2 = "4142135623730950488016887242096980785696718753769480731766797379907324784621" \
"07038850387534327641572735013846230912297024924836055850737212644121497099935831" \
"41322266592750559275579995050115278206057147010955997160597027453459686201472851" \
"74186408891986095523292304843087143214508397626036279952514079896872533965463318" \
"08829640620615258352395054745750287759961729835575220337531857011354374603408498" \
"84716038689997069900481503054402779031645424782306849293691862158057846311159666" \
"87130130156185689872372352885092648612494977154218334204285686060146824720771435" \
"85487415565706967765372022648544701585880162075847492265722600208558446652145839" \
"88939443709265918003113882464681570826301005948587040031864803421948972782906410" \
"45072636881313739855256117322040245091227700226941127573627280495738108967504018" \
"36986836845072579936472906076299694138047565482372899718032680247442062926912485" \
"90521810044598421505911202494413417285314781058036033710773091828693147101711116" \
"83916581726889419758716582152128229518488472089694633862891562882765952635140542" \
"26765323969461751129160240871551013515045538128756005263146801712740265396947024" \
"03005174953188629256313851881634780015693691768818523786840522878376293892143006" \
"55869568685964595155501644724509836896036887323114389415576651040883914292338113" \
"20605243362948531704991577175622854974143899918802176243096520656421182731672625" \
"75395947172559346372386322614827426222086711558395999265211762526989175409881593" \
"48640083457085181472231814204070426509056532333398436457865796796519267292399875" \
"36661721598257886026336361782749599421940377775368142621773879919455139723127406" \
"68983299898953867288228563786977496625199665835257761989393228453447356947949629" \
"52168891485492538904755828834526096524096542889394538646625744927556381964410316" \
"97983306185201937938494005715633372054806854057586799967012137223947582142630658" \
"51322174088323829472876173936474678374319600015921888073478576172522118674904249"

e = "7182818284590452353602874713526624977572470936999595749669676277240766303535475945" \
"7138217852516642742746639193200305992181741359662904357290033429526059563073813232" \
"8627943490763233829880753195251019011573834187930702154089149934884167509244761460" \
"6680822648001684774118537423454424371075390777449920695517027618386062613313845830" \
"0075204493382656029760673711320070932870912744374704723069697720931014169283681902" \
"5515108657463772111252389784425056953696770785449969967946864454905987931636889230" \
"0987931277361782154249992295763514822082698951936680331825288693984964651058209392" \
"3982948879332036250944311730123819706841614039701983767932068328237646480429531180" \
"2328782509819455815301756717361332069811250996181881593041690351598888519345807273" \
"8667385894228792284998920868058257492796104841984443634632449684875602336248270419" \
"7862320900216099023530436994184914631409343173814364054625315209618369088870701676" \
"8396424378140592714563549061303107208510383750510115747704171898610687396965521267" \
"1546889570350354"

phi = "61803398874989484820458683436563811772030917980576286213544862270526046281890244" \
"97072072041893911374847540880753868917521266338622235369317931800607667263544333" \
"89086595939582905638322661319928290267880675208766892501711696207032221043216269" \
"54862629631361443814975870122034080588795445474924618569536486444924104432077134" \
"49470495658467885098743394422125448770664780915884607499887124007652170575179788" \
"34166256249407589069704000281210427621771117778053153171410117046665991466979873" \
"17613560067087480710131795236894275219484353056783002287856997829778347845878228" \
"91109762500302696156170025046433824377648610283831268330372429267526311653392473" \
"16711121158818638513316203840052221657912866752946549068113171599343235973494985" \
"09040947621322298101726107059611645629909816290555208524790352406020172799747175" \
"34277759277862561943208275051312181562855122248093947123414517022373580577278616" \
"00868838295230459264787801788992199027077690389532196819861514378031499741106926" \
"08867429622675756052317277752035361393621076738937645560606059216589466759551900" \
"40055590895022953094231248235521221241544400647034056573479766397239494994658457" \
"88730396230903750339938562102423690251386804145779956981224457471780341731264532" \
"20416397232134044449487302315417676893752103068737880344170093954409627955898678" \
"72320951242689355730970450959568440175551988192180206405290551893494759260073485" \
"22821010881946445442223188913192946896220023014437702699230078030852611807545192" \
"88770502109684249362713592518760777884665836150238913493333122310533923213624319" \
"26372891067050339928226526355620902979864247275977256550861548754357482647181414" \
"51270006023890162077732244994353088999095016803281121943204819643876758633147985"

pi = "14159265358979323846264338327950288419716939937510582097494459230781640628620899" \
"86280348253421170679821480865132823066470938446095505822317253594081284811174502" \
"84102701938521105559644622948954930381964428810975665933446128475648233786783165" \
"27120190914564856692346034861045432664821339360726024914127372458700660631558817" \
"48815209209628292540917153643678925903600113305305488204665213841469519415116094" \
"33057270365759591953092186117381932611793105118548074462379962749567351885752724" \
"89122793818301194912983367336244065664308602139494639522473719070217986094370277" \
"05392171762931767523846748184676694051320005681271452635608277857713427577896091" \
"73637178721468440901224953430146549585371050792279689258923542019956112129021960" \
"86403441815981362977477130996051870721134999999837297804995105973173281609631859" \
"50244594553469083026425223082533446850352619311881710100031378387528865875332083" \
"81420617177669147303598253490428755468731159562863882353787593751957781857780532" \
"1712268066130019278766111959092164201989"

