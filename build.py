def build():
    from os import system as cmd
    from editor import edit

    cmd("rm -rf package/dist")
    cmd("mkdir package/dist")
    cmd("clear")
    useEditor = input("Run Version Editor (Y|*)? ").upper()
    if useEditor == "Y":
        edit()
    cmd("clear")
    print("Run these commands next: \n  cd package\n  ./upload.sh")
    cmd("bash")
