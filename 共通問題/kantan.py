def kansu(ans = "?"):
    listA = list(range(2,500,3))
    if ans in listA:
        return "正解"
    elif ans == "?":
        return
    else:
        return "不正解"

