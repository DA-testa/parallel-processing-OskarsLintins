# python3

def parallel_processing(n, m, data):
    output = []
    rinda = [(i, 0) for i in range(n)]

    for i in range(m):
        time = data[i]
        thread, timeStart = rinda.pop(0)
        timeEnd = timeStart + time
        output.append((thread, timeStart))
        rinda.append((thread, timeEnd))
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)

    for thread, timeStart in result:
        print(thread, timeStart)

if __name__ == "__main__":
    main()
