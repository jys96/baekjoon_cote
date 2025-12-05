while True:
    try:
        input_str = input()

        if input_str:
            A, B = map(int, input_str.split())
            
            print(A + B)
        else:
            break
    except EOFError:
        break
    except:
        break
