import rsm

if __name__ == '__main__':
    with open("RSMFiles/TravisWight.rsm", "r+") as test:
        r = rsm.RSM(test)
        print(r.meta["NUM_PAGES"])