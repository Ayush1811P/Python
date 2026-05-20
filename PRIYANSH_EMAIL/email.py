def mail(M):
    is_correct=False
    a=b=c=d=e=0
    if len(M)>=9:
        a=1
        if M[0].isalpha():
            b=1
            for i in M:
                if M.count("@")==1:
                    c=1
                    if M.count(".")==1:
                        is_correct=True
                        d=1
                        e=1                       
    return is_correct






