import json

contests = tuple(["abc","arc","agc"])
contests_full = {"Atcoder":{"abc":["atcoder beginner contest","H_Ex"],"arc":["atcoder regular contest","F"],"agc":["atcoder grand contest","F"],"Problems":["A","B","C","D","E","F","G","H_Ex"]}}

intro_base = "作成するファイルを数字又はidで選択してください。 -> [$ Cmd >> Contests Option]\n"
intro_contest = "Contests:\n\t1:abc 2:arc 3:agc\n"
intro_option = "option:\n\t-skip:<num> \t[num番のファイルを生成します。既定では前回生成した次の番号のファイルが生成されます。]\n\t-prob:<id> \t[idまでの問題回答ファイルを生成します。idが無効である場合は通常通りに作成します。]\n\t-file:<name> \t[拡張子をnameとしてファイルを生成します。デフォルトではpyが選択されます]\n"
intro_end = "$ Cmd >> "
intro = intro_base + intro_contest + intro_option + intro_end

def json_update(id):
    make_file_num = open(f"./_sys/{id}.json","r")
    json_file = json.load(make_file_num)
    make_file_num.close()
    json_file["num"] += 1
    write_file = open(f"./_sys/{id}.json","w")
    json.dump(json_file,write_file,indent=4)

def make_file(id : str,file_num : int,site : str,options : dict):
    from os import makedirs
    try:
        makedirs(f"./{contests_full[site][id][0]}/{id.upper()}{file_num}")
    except:
        print(f"Error No.201 : 既に該当コンテストのフォルダが生成されています(./{contests_full[site][id][0]}/{id.upper()}{file_num})")
    for problems in contests_full[site]["Problems"]:
        try:
            open(f"./{contests_full[site][id][0]}/{id.upper()}{file_num}/{problems}.{options['file']}","r")
            print(f"Error No.201 : 既に該当問題のファイルが生成されています(./{contests_full[site][id][0]}/{id.upper()}{file_num}/{problems}.{options['file']})")
        except:
            open(f"./{contests_full[site][id][0]}/{id.upper()}{file_num}/{problems}.{options['file']}","w")
        if problems == contests_full[site][id][1] or problems == options["prob"]:
            print(f"Success : {contests_full[site][id][0]} : {id.upper()}{file_num}のフォルダとファイル生成が完了しました")
            break

def get_file(id,options):
    try:
        make_file_num = open(f"./_sys/{id}.json","r")
    except:
        write_file = open(f"./_sys/{id}.json","w")
        write_file.write("{\n\t\"num\":0\n}")
        write_file.close()
        make_file_num = open(f"./_sys/{id}.json","r")
    json_file = json.load(make_file_num)
    default_file = "py"
    limit_prob = "Unknown"
    for option in options:#オプションの中身を走査
        part,choice = option.split(":")
        if part == "-skip":
            try:
                json_file["num"] = int(choice)
            except:
                print("Error No.301 : option -skipの読み取りに失敗しました。(入力された値が不正です)")
                exit()
        if part == "-file":
            default_file = choice
        if part == "-prob":
            limit_prob = choice
    write_file = open(f"./_sys/{id}.json","w")
    json.dump(json_file,write_file,indent=4)
    make_file_num.close()
    options = {"file":default_file,"prob":limit_prob}
    return json_file["num"],options

def get_site(id):
    if id == "abc" or id == "arc" or id == "agc": return "Atcoder"
    return "Error"

def get_mode():
    """
    Args :
        None
    Returns :
        追加するファイルを指定するコンテスト(id[0])
        追加オプション文字列               (id[1])
    """
    while True:
        id = list(input(intro).split())
        try:  
            id_num = int(id[0]) #一文字目を
            if 1 <= id_num and id_num <= 3:
                id = [contests[id_num - 1]]
                break
        except: 
            pass
        if id[0] in contests:
            break
        elif id[0].lower() == "exit": return "Exit",None
        else:
            print("指定された選択肢から選択して下さい")
        try: id[1:]
        except: id.append("")
    return id[0],id[1:]

if __name__ == "__main__":
    while True:
        id,option = get_mode()
        if id == "Exit": break
        site = get_site(id)
        if site == "Error" : print("Error No.101 : 該当コンテストに当てはまるサイトが登録されていません")
        make_num,options = get_file(id,option)
        make_file(id,make_num,site,options)
        json_update(id)