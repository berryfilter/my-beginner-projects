# return masked string
"""cc = "4321632"
def maskify(cc):
    if len(cc) > 4:
        masked_part = "".join(["#" for ch in cc[:-4]])
        reg_part = cc[-4:]
        cc_masked = masked_part + reg_part
        return cc_masked
    else:
        return cc


print(maskify(cc))"""

"""def maskify(cc):
    return "".join(["#" for ch in cc[:-4]]) + cc[-4:] if len(cc) > 4 else cc
print(maskify(cc))"""

"""cc = "osaidhnoiaw"


def maskify(cc):
    if len(cc) <= 4:
        return cc

    mask_cc = "".join("#" for i in cc[:-4])
    cc_normal = cc[-4:]
    return(mask_cc + cc_normal)

print(maskify(cc))
"""
"""
mixed = ["code", 7, "arcane", None, "python", 3.14]
print(" - ".join(i for i in mixed if isinstance(i, str)))

print(" ".join(i for i in mixed if isinstance(i, str)) )

"""










cc = "3948739"


"""def maskify(cc):
    if len(cc) > 4:
        cc_mask = "".join("#" for i in cc[:-4])
        return cc_mask + cc[-4:]
    else:
        return cc
        
        

def maskify(cc):
    return ("".join("#" for i in cc[:-4]) + cc[-4:] if len(cc) > 4 else cc)

print(maskify(cc))


cc_mask = "".join('#' for i in cc)

print(cc_mask)

"""





















