def draw_money(request,money):
    if request > money :
        print "Low Account Credit"
    else:
        while request > 0:
            if request >= 5:
                if request >= 10:
                    if request >= 20:
                        if request >= 50:
                            if request >= 100:
                                print 100
                                request = request -100
                            else:
                                print 50
                                request = request - 50
                        else:
                            print 20
                            request=request-20
                    else:
                        print 10
                        request=request-10
                else:
                    print 5
                    request = request- 5
            else:
                print request
                request = 0

draw_money(477,600)
