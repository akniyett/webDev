def cigar_party(cigars, is_weekend):
    if is_weekend == True:
        return 40 <= cigars
    else: 
        return 40 <= cigars <= 60
