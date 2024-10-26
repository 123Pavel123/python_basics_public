plaves = False
behas = True

## 1
print("varianta 1\n##########")
if plaves:
    print("ano, plavu")  # if a
elif behas:
    print("ano, beham")  # if a and b
else:
    print("mel bys se sebou neco delat")

print("bezim zitra na bazen, bezis se mnou?\n\n")


# 2
print("varianta 2\n##########")
if plaves:
    print("ano, plavu")  # if a
    if behas:
        print("ano, beham")  # if a and b
else:
    print("mel bys se sebou neco delat")

print("bezim zitra na bazen, bezis se mnou?\n\n")

# 3
print("varianta 3\n##########")
if plaves:
    print("ano, plavu")  # if a
if behas:
    print("ano, beham")  # if a and b
else:
    print("mel bys se sebou neco delat")

print("bezim zitra na bazen, bezis se mnou?\n\n")

# 4 stejne jako 1
print("varianta 4 stejna jako 1\n########################")
if plaves:
    print("ano, plavu")  # if a
else:
    if behas:
        print("ano, beham")  # if a and b
    else:
        print("mel bys se sebou neco delat")

print("bezim zitra na bazen, bezis se mnou?\n\n")
