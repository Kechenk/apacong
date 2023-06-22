def remove_words_from_txt(input_file_path, output_file_path, words_to_remove):
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()

    for word in words_to_remove:
        content = content.replace(word, '')

    with open(output_file_path, 'w') as output_file:
        output_file.write(content)

input_file_path = "input.txt"  # Path to the input text file
output_file_path = "output.txt"  # Path to the output text file

words_to_remove = [
    "ONLINE", "SHOP", "OUTLET", "SMART", "LIVING", "WASH", "CAR",
    "MODIFIKASI", "MODIF", "CLOTHING", "MERCH", "AUTO", "RECORDS",
    "FLOWER", "FLORIST", "SKIN", "CARE", "TRAVEL", "JOGJA", "SURABAYA",
    "MALANG", "MAKASSAR", "BEKASI", "MOBIL", "WARNA", "VARIASI", "GROSIR",
    "ECER", "BEAUTY", "SUKSES", "TELESKOP", "STORE", "ONLEN",
    "VARIASI", "GADGET", "SAFETY", "SECOND", "SNACK", "TIME", "ARLOJI", "HIJAB",
    "SALJU", "ELEKTRONIK", "STYLE", "TOKOPEDIA LOADTEST", "COMPUTER", "BEER", "COMPANY",
    "TROOPER", "PALINGMURAH", "TRANSAKSI", "GROUP", "JAS", "HUJAN", "SOLO",
    "SQUARE", "KAOS", "BOLA", "PREMIUM", "TOKO", "KARYA", "MANDIRI", "VAPE", "CREATIVE",
    "BAKUL", "CILIK", "CLOTH", "TEKNIK", "CREATOR", "SWALAYAN", "MURAH", "DEMAK",
    "ENGINE", "TECH", "KEGELAPAN", "COSMETICS", "BOX", "HIDDEN", "WATCH", "EXPERT",
    "POSITIVE", "MENTAL", "ATTITUDE", "HARDROCK", "GREEDY", "ZOONE", "ZONE", "SNEAKERS",
    "GANTENG", "GIRL", "CHANNEL", "COLLECTION", "LIFESTYLE", "FLYING", "POTATO", 
    "NOT ", "FOR", "PRINCE", "SAJADAH", "PT ", "PLAFON", "ROOF", "TB", "BOOKSTORE", "CANTIQ",
    "KAK", "AHLI ", "SPARE", "PART", "NISSAN", "MUSIC", "IAM ", "YOUR", "DREAM", "KENDAL",
    "KOTA", "SOVENIR", "UNIK", "IDEA", "UVUVWEVWEVWE", "ROCK", "CUCIGUDANGORIFLAME", "PALINGMURAH",
    "PC", "BERANDALAN", "VROOMSONE", "BIKERS", "CLOTH", "JASA", "PERIZINAN", "MAKEUPADDICT",
    "KABOELL", "PENGHUNI", "BRAJA", "CITYY", "PROCOMPUTER", "STARK", "PENULIS", "GAGAL", "ANAKNYA", "BUNDHAAYAHIWAN",
    "PREMIUM", "JINX", "CSC", "MAKASSAR", "FASHION", "RADIO", "SKAK", "SLIME", "CMEARTHSLIME",
    "ACSESORIS", "AKSESORIS", "ACC", "PASTIBAGUS", "DEH", "AYAM", "PELUNG", "BANDUNG", "ASBAK", "OLSHOP", 
    "HERBS ", "COMP", "GUDANG", "GAMERS", "AGEN "

]

remove_words_from_txt(input_file_path, output_file_path, words_to_remove)
